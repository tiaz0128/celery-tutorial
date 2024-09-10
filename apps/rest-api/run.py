import os
from random import randint
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from rabbit import RabbitQueue

load_dotenv()

app = FastAPI()

url = os.getenv("RABBITMQ_URL")
user = os.getenv("RABBITMQ_DEFAULT_USER")
pwd = os.getenv("RABBITMQ_DEFAULT_PASS")


@app.get("/")
def read_root():
    return PlainTextResponse("healthy")


@app.get("/publish")
def publish_task():
    queue = RabbitQueue(url, user, pwd)

    a = randint(1, 100)
    b = randint(1, 100)

    queue.publish_task(service="FastAPI", a=a, b=b)

    return PlainTextResponse(f"FastAPI : {a=},{ b=} Published to the queue")
