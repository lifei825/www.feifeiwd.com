FROM python:2.7.13-alpine
MAINTAINER lifei5 "lifei5@asiainfo.com"

RUN apk update && apk add ca-certificates tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

COPY . /home/django

RUN apk add nginx supervisor mariadb-dev g++ python-dev \
    && mkdir /etc/supervisor.d && mkdir -p /home/django && mkdir /run/nginx && \
    pip install -r /home/django/requirements.txt

# RUN echo_supervisord_conf > /etc/supervisord.conf

COPY config/nginx.conf /etc/nginx/
COPY config/*.ini /etc/supervisor.d/
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
