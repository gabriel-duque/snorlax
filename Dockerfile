FROM python:alpine

LABEL maintainer="Gabriel Duque <gabriel@zuh0.com> (zuh0)"

LABEL org.label-schema.build-date="$BUILD_DATE"

LABEL org.label-schema.name="snorlax"

LABEL org.label-schema.description="A Django-based website for cooking recipes."

LABEL org.label-schema.url="https://recipes.zuh0.com"

LABEL org.label-schema.vcs-url="https://github.com/zuh0/snorlax"

LABEL org.label-schema.vcs-ref="$VCS_REF"

LABEL org.label-schema.version="$VERSION"

LABEL org.label-schema.schema-version="1.0"

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
