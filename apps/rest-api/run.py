import os
from random import randint
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from celery import Celery
from celery import group, chain, chord, signature

load_dotenv()

app = FastAPI()

url = os.getenv("RABBITMQ_URL")
user = os.getenv("RABBITMQ_DEFAULT_USER")
pwd = os.getenv("RABBITMQ_DEFAULT_PASS")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")  # Redis URL 명확하게 설정

celery = Celery(
    "Math Operations",
    broker=f"pyamqp://{user}:{pwd}@{url}//",
    backend=REDIS_URL,
)


@app.get("/")
def read_root():
    return PlainTextResponse("healthy")


@app.get("/task/{task_id}")
async def get_task_result(task_id: str):
    result = celery.AsyncResult(task_id)
    return {"task_id": task_id, "status": result.status, "result": result.result}


@app.get("/publish")
def publish_task():
    a = randint(1, 100)
    b = randint(1, 100)

    celery.send_task(
        "tasks.math.sum",
        kwargs={"service": "FastAPI", "a": a, "b": b},
        queue="sum-queue",
    )

    return PlainTextResponse(f"FastAPI : {a=},{ b=} Published to the queue wait...")


@app.get("/parallel")
async def parallel_operation():
    task_group = group(
        signature(
            "tasks.math.sum",
            kwargs={"service": "FastAPI", "a": 2, "b": 2},
            queue="sum-queue",
        ),
        signature(
            "tasks.math.sum",
            kwargs={"service": "FastAPI", "a": 3, "b": 3},
            queue="sum-queue",
        ),
    )

    callback = signature("tasks.math.multiply", queue="multiply-queue")

    result = chord(task_group)(callback)

    return PlainTextResponse(f"Task Submitted, Result ID: {result.id}")
