from celery import shared_task


@shared_task
def add(x, y):
    return x + y


# from run import app


# @app.task
# def add(x, y):
#     return x + y
