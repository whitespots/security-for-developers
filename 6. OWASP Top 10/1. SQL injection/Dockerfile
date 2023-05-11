FROM python:3-alpine3.12
RUN adduser -D -u 1001 whitespots whitespots

COPY . .

RUN set -xe \
    && apk add --no-cache git jq curl \
    && python -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

USER whitespots
ENTRYPOINT ["python", "server.py"]
