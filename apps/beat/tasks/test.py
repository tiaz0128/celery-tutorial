from run import app


@app.task(queue="test-queue")
def schedule_test():
    kwargs = {
        "a": 1,
        "b": 2,
        "c": 3,
    }

    app.send_task(
        "tasks.test.consume_task",
        kwargs=kwargs,
        queue="dclo-report-start",
    )

    return {"message": "Report task added to the queue"}

    # webinars = get_today_webinars(user_email)

    # for eta_time, url, elapsed_time in webinars:
    #     expires_time = (datetime.fromisoformat(eta_time) + timedelta(seconds=elapsed_time)).isoformat()

    #     # celery 실행
    #     run_web_page_task.apply_async(
    #         args=[url, elapsed_time],
    #         eta=eta_time,
    #         expires=expires_time,
    #     )

    return "Success"
