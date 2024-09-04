import logging
import os
from run import app


@app.task(queue="test-queue")
def consume_task(a, b, c):
    logging.info(f"Worker Start")
    logging.info(f"{a=}, {b=}, {c=}")

    return "Worker Done"
