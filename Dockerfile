FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

RUN apk update \
    && apk add --no-cache \
        python3-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./entrypoint.sh /code/entrypoint.sh
RUN chmod 744 /code/entrypoint.sh

COPY ./app /code/app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && chown appuser:appgroup /code
USER appuser

EXPOSE 8000

CMD ["./entrypoint.sh"]
