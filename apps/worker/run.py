from celery import Celery


app = Celery(
    "Celery Worker",
    include=[
        "tasks.sum",
        "tasks.schedule",
    ],
)

app.config_from_object("config")
