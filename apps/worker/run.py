from celery import Celery

app = Celery(
    "Celery Worker",
    include=[
        "tasks.sum",
    ],
)

app.config_from_object("celeryconfig")
