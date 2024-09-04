import logging
from celery import Celery


class RabbitQueue:
    __instance = None
    __celery_app = None

    def __new__(cls, url, username, password):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__celery_app = Celery(
                "my_celery_app",
                broker=f"pyamqp://{username}:{password}@{url}//",
            )

        return cls.__instance

    # Celery 작업을 큐에 추가합니다.
    def publish_task(self, **kwargs):
        logging.info(f"Publishing task to the queue: {kwargs}")
        
        self.__celery_app.send_task(
            "tasks.test.consume_task",
            kwargs=kwargs,
            queue="test-queue",
        )

        
