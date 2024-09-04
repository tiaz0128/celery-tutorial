# celery tutorial

## 환경 세팅

### RabbitMQ Docker

```bash
$ docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

### fast-api (publisher)

### celery beat

### celery worker

## Docker Compose

```bash
$ docker-compose up --build
```
