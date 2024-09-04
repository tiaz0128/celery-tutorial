import os

from dotenv import load_dotenv

load_dotenv()


url = os.getenv("DCLO_RABBITMQ_REPORT_SQS")
user = os.getenv("DCLO_RABBITMQ_DEFAULT_USER")
pwd = os.getenv("DCLO_RABBITMQ_DEFAULT_PASS")

broker_url = f"pyamqp://{user}:{pwd}@{url}//"

result_backend = "redis://localhost:6379/0"

task_serializer = "json"
accept_content = ["json"]
result_serializer = "json"
enable_utc = True
timezone = "UTC"
broker_connection_retry_on_startup = True
