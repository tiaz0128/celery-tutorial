import logging

from run import app


@app.task(queue="sum-queue")
def sum(service, a, b):
    logging.info(f"Worker Start : {service=}")
    logging.info(f"{a=}, {b=}")
    logging.info(f"Task Done : {a} + {b} = {a + b}")

    return a + b


@app.task(queue="multiply-queue")
def multiply(nums):

    logging.info(f"multiply nums : {nums}")
    x, y = nums
    result = x * y

    # logging.info(f"Worker Start : {service=}")
    logging.info(f"{x=}, {y=}")
    logging.info(f"Task Done : {x} * {y} = {result}")

    return result
