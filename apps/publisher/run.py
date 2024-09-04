import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from rabbit import RabbitQueue

load_dotenv()

app = FastAPI()

url = os.getenv("DCLO_RABBITMQ_REPORT_SQS")
user = os.getenv("DCLO_RABBITMQ_DEFAULT_USER")
pwd = os.getenv("DCLO_RABBITMQ_DEFAULT_PASS")


@app.get("/")
def read_root():
    return PlainTextResponse("healthy")


@app.get("/test")
def publish_test():
    queue = RabbitQueue(url, user, pwd)

    queue.publish_task(a=1, b=2, c=3)

    return PlainTextResponse("success")
