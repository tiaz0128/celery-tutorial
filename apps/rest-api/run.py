from random import randint
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from celery import Celery

app = FastAPI()

url = "localhost"
username = "guest"
password = "guest"

celery = Celery(
    "Client App",
    broker=f"pyamqp://{username}:{password}@{url}//",
    backend=f"redis://{url}:6379/0",
)

@app.get("/publish")
def publish_task():

    a = randint(1, 100)
    b = randint(1, 100)

    celery.send_task(
        "tasks.sum.consume_task",
        kwargs={"a": a, "b": b},
        queue="sum-queue",
    )

    return PlainTextResponse(f"FastAPI : {a=},{ b=} Published to the queue")
