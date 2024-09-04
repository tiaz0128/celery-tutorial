from celery import Celery


app = Celery(
    "Celery Worker",
    include=[
        "tasks.test",
    ],
)

app.config_from_object("config")

if __name__ == "__main__":
    app.start()
