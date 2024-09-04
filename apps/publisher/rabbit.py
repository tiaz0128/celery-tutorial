from beat.rabbit import Celery

from base import BaseQueue


class RabbitQueue(BaseQueue):
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

    def make_channel(func):
        def wrapper(self, *args, **kwargs):
            self.channel = self._connection.channel()
            result = func(self, *args, **kwargs)
            self.channel.close()

            return result

        return wrapper

    def publish(self, data: dict):
        return self.start_report(**data)

    # Celery 작업을 큐에 추가합니다.
    def start_report(self, **kwargs):
        self.__celery_app.send_task(
            "app.tasks.start.start_report",
            kwargs=kwargs,
            queue="dclo-report-start",
        )

        return {"message": "Report task added to the queue"}
