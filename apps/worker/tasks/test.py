import logging

from run import app



@app.task(queue="test-queue")
def consume_task(service, a, b, c):
    logging.info(f"Worker Start : {service=}")
    logging.info(f"{a=}, {b=}, {c=}")
    logging.info(f"Task Done : {a} + {b} + {c} = {a+b+c}")

    return a+b+c
