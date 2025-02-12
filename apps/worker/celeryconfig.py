broker_url = "pyamqp://guest:guest@localhost//"
result_backend = "redis://localhost:6379/0"

task_serializer = "json"
accept_content = ["json"]
result_serializer = "json"
enable_utc = True
timezone = "UTC"
broker_connection_retry_on_startup = True
