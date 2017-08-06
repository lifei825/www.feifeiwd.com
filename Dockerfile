FROM python:2.7.13-alpine
MAINTAINER lifei5 "lifei5@asiainfo.com"

RUN apk update && apk add ca-certificates && \
    apk add tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

COPY . /home/django

RUN apk add nginx && apk add supervisor && mkdir /etc/supervisor.d && mkdir -p /home/django && \
    pip install -r requirements.txt

# RUN echo_supervisord_conf > /etc/supervisord.conf

COPY congig/nginx.conf /etc/nginx/
COPY config/*.ini /etc/supervisor.d/
COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
