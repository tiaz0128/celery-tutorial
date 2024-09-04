import logging
from run import app


@app.task(queue="beat-queue")
def schedule_test():
    logging.info("Task published to the queue")
