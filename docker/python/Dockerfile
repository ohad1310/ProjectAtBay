FROM python:alpine
RUN apk add --update \
        coreutils \
    && rm -rf /var/cache/apk/*
RUN pip install flask
ADD Python_Flask_CRUD/. /
CMD ["python","main.py"]