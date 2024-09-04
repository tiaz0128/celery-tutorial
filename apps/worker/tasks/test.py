import logging

from run import app
from random import randint


@app.task(queue="beat-queue")
def schedule_test():
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)

    app.send_task(
        "tasks.test.consume_task",
        kwargs={"a": a, "b": b, "c": c},
        queue="test-queue",
    )

    return {"message": f"Beat task added to the queue: {a=}, {b=}, {c=}"}


@app.task(queue="test-queue")
def consume_task(a, b, c):
    logging.info(f"Worker Start")
    logging.info(f"{a=}, {b=}, {c=}")

    return f"Worker Done : {a=}, {b=}, {c=}"
