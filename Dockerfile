FROM python:alpine

RUN apk add --no-cache \
            gcc \
            g++ \
            libffi-dev \
            musl-dev \
            openssl-dev

COPY requirements.txt snorlax ./

RUN pip install -r requirements.txt

WORKDIR snorlax

RUN mkdir persistent && chown 1000:1000 persistent

USER 1000:1000

VOLUME persistent

ENTRYPOINT ["/snorlax/snorlax.sh"]
