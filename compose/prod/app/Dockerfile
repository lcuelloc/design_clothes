FROM python:3.7.0-alpine3.8

ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=config.settings.production

RUN set -ex && mkdir /code/
WORKDIR /code/

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

RUN set -ex \
\
    # replacing default repositories with edge ones
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" > /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "http://dl-5.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories \
\
    && apk add --no-cache build-base linux-headers \
        # psycopg2 dependencies
        musl-dev postgresql-dev perl file libxml2-dev libgcc postgresql-client \
        # GeoDjango dependecies
        gdal-dev geos-dev geos gdal binutils
        #proj4

#RUN ln -s /usr/lib/libproj.so.0 /usr/lib/libproj.so
RUN set -ex && pip install pip --upgrade
RUN set -ex && pip install pipenv
RUN set -ex && pipenv install --system --skip-lock

COPY ./compose/prod/app/start.sh /start.sh
COPY ./compose/prod/app/entrypoint.sh /entrypoint.sh
RUN set -ex && chmod +x /start.sh
RUN set -ex && chmod +x /entrypoint.sh

COPY . /code/

ENTRYPOINT ["/entrypoint.sh"]


