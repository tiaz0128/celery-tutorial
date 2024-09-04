# Celery tutorial

Celery를 사용하여 RabbitMQ로 publish / consume 처리 하기

1. REST API(FastAPI)에서 MQ로 publish
2. Celery Beat에서 MQ로 publish
3. Celery Work에서 consume

## 로컬 환경 세팅

### python 세팅

- poetry로 설치

```bash
poety install
```

### .env

- 로컬에서 사용할 `.env` 파일 루트 경로에 생성

```text
RABBITMQ_URL=localhost
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest

REDIS_URL=localhost
```

### RabbitMQ Docker

```bash
$ docker run -d -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

### redis Docker

```bash
$ docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

## Docker Compose

```bash
$ docker-compose up --build
```
