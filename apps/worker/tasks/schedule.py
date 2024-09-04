from random import randint

from run import app


@app.task(queue="beat-queue")
def schedule_task():
    a = randint(1, 100)
    b = randint(1, 100)
    c = randint(1, 100)

    app.send_task(
        "tasks.test.consume_task",
        kwargs={"service":"Beat", "a": a, "b": b, "c": c},
        queue="test-queue",
    )

    return {"message": f"Beat : task added to the queue: {a=}, {b=}, {c=}"}