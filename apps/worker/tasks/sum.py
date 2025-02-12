import logging
import time

from run import app

@app.task(queue="sum-queue")
def consume_task(a, b):
    time.sleep(5)

    logging.info(f"{a=}, {b=}")
    logging.info(f"Task Done : {a} + {b} = {a + b}")

    return a + b
