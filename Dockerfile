# pull official base image
FROM python:3.10.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# making the script executable
RUN chmod +x docker-entrypoint.sh

EXPOSE 5000
#EXPOSE 5432

RUN ls -la app/

CMD ["./docker-entrypoint.sh"]
#ENTRYPOINT [ "./docker-entrypoint.sh" ]
#CMD ["gunicorn", "--workers", "8", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "app:app"]