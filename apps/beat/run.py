from celery import Celery
from celery.beat import crontab

app = Celery(
    "Celery Beat",
    include=[
        "tasks.schedule",
    ],
)
app.config_from_object("celeryconfig")

# task 함수 주기 설정
app.conf.beat_schedule = {
    "add-every-seconds": {
        "task": "tasks.schedule.schedule_task",
        # "schedule": crontab(minute=0),  # 매 시간마다
        "schedule": 30,  # 30초마다
    },
}


if __name__ == "__main__":
    app.start()
