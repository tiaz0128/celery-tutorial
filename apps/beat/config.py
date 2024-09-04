import os

from dotenv import load_dotenv

load_dotenv()


url = os.getenv("RABBITMQ_URL")
user = os.getenv("RABBITMQ_DEFAULT_USER")
pwd = os.getenv("RABBITMQ_DEFAULT_PASS")

broker_url = f"pyamqp://{user}:{pwd}@{url}//"

redis_url = os.getenv("REDIS_URL", "localhost")
result_backend = f"redis://{redis_url}:6379/0"

task_serializer = "json"
accept_content = ["json"]
result_serializer = "json"
enable_utc = True
timezone = "UTC"
broker_connection_retry_on_startup = True

beat_schedule_filename = "./.temp/celerybeat-schedule"
