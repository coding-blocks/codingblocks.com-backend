FROM python:3.8.2-alpine

RUN apk update
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv

WORKDIR /usr/src/cbdb

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system
RUN pip install gunicorn

COPY . .

ENTRYPOINT [ "gunicorn", "cbdb.wsgi", "-b", "0.0.0.0:8000"]