FROM python:3.9-alpine
RUN apk update && apk upgrade && apk add gcc musl-dev libc-dev libc6-compat linux-headers build-base git libffi-dev openssl-dev
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
ADD main.py /app
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:5000", "main:app"]