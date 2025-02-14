from celery import Celery

app = Celery(
    "Celery App",
    broker="pyamqp://guest:guest@localhost//",
    broker_connection_retry_on_startup=True,
    include=["tasks.math"],
)

# from tasks.math import add

# app.register_task(add, name="add")
