import logging

from run import app


@app.task(queue="test-queue")
def consume_task(service, a, b):
    logging.info(f"Worker Start : {service=}")
    logging.info(f"{a=}, {b=}")
    logging.info(f"Task Done : {a} + {b} = {a + b}")

    return a + b
