import logging
from random import randint
from time import sleep

from run import app


@app.task(queue="hello-queue")
def hello():
    time = randint(1, 5)
    sleep(time)
    logging.info(f"Worker Hello")

    return "Hello"


@app.task(queue="world-queue")
def world():
    time = randint(1, 5)
    sleep(time)
    logging.info(f"Worker World")

    return "World"


@app.task(queue="concat-queue")
def concat_words(words):
    logging.info(f"Concat recived Words : {words}")

    return "{0} {1} Celery!".format(*words)
