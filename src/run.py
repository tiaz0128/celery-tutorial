from celery import Celery

app = Celery(
    "tasks",
    broker="pyamqp://guest:guest@localhost//",
    # backend="redis://localhost/0",
    broker_connection_retry_on_startup=True,
    include=["tasks.math"],
)
