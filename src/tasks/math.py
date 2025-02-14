from time import sleep
from celery import shared_task


@shared_task
def add(x, y):
    sleep(30)
    return x + y


# from run import app


# @app.task
# def add(x, y):
#     return x + y
