FROM python:alpine

RUN apk add --no-cache \
            gcc \
            libffi-dev \
            musl-dev \
            openssl-dev

COPY requirements.txt snorlax ./

RUN pip install -r requirements.txt

RUN apk del --purge gcc

USER 1000:1000

WORKDIR snorlax

ENTRYPOINT ["/snorlax/snorlax.sh"]
