FROM python:3.8.2-alpine

RUN apk update
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev nginx

RUN pip install pipenv

WORKDIR /usr/src/cbdb

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile
RUN pip install gunicorn
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
RUN mkdir -p /run/nginx

COPY . .
RUN python manage.py collectstatic --no-input

ENTRYPOINT [ "./bin/start.sh" ]