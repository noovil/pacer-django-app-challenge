FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


COPY . /app/backend/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]