from run import app


@app.task(queue="beat-queue")
def schedule_task():
    pass
