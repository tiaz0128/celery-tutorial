from celery import Celery


app = Celery(
    "Celery Worker",
    include=[
        "tasks.math",
        "tasks.schedule",
    ],
)

app.config_from_object("celeryconfig")
