import logging
from celery import Celery


class RabbitQueue:
    _instance = None
    _celery_app = None

    def __new__(cls, url, username, password):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._celery_app = Celery(
                "my_celery_app",
                broker=f"pyamqp://{username}:{password}@{url}//",
            )

        return cls._instance

    # Celery 작업을 큐에 추가합니다.
    def publish_task(self, **kwargs):
        logging.info(f"Publishing task to the queue: {kwargs}")

        self._celery_app.send_task(
            "tasks.sum.consume_task",
            kwargs=kwargs,
            queue="sum-queue",
        )
