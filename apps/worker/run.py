from celery import Celery


app = Celery(
    "Celery Worker",
    include=[
        "tasks.math",
        "tasks.schedule",
        "tasks.word",
    ],
)

app.config_from_object("celeryconfig")
