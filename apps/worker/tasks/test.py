import logging

from run import app
from random import randint


@app.task(queue="beat-queue")
def schedule_test():
    kwargs = {
        "a": randint(1, 100),
        "b": randint(1, 100),
        "c": randint(1, 100),
    }

    app.send_task(
        "tasks.test.consume_task",
        kwargs=kwargs,
        queue="test-queue",
    )

    return {"message": "Report task added to the queue"}


@app.task(queue="test-queue")
def consume_task(a, b, c):
    logging.info(f"Worker Start")
    logging.info(f"{a=}, {b=}, {c=}")

    return "Worker Done"
