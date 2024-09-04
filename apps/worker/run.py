from celery import Celery


app = Celery(
    "Celery Worker",
    include=[
        "tasks.test",
    ],
)

# MQ 인 경우 변경 필요
app.config_from_object("config")

if __name__ == "__main__":
    app.start()
