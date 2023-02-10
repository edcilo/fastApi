FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production
ENV APP_NAME=app
ENV APP_VERSION=1.0.0

RUN apk update \
    && apk add --no-cache \
        build-base \
        postgresql-dev \
        python3-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
RUN chmod 744 /code/entrypoint.sh
RUN pip install -e .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && chown appuser:appgroup -R /code
USER appuser

EXPOSE 8000

CMD ["./entrypoint.sh"]
