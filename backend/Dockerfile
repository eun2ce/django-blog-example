# syntax=docker/dockerfile:1
FROM python:3.5

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/backend/
WORKDIR /app/backend

RUN pip install -r requirements.txt

EXPOSE 8000

#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python manage.py migrate; python manage.py runserver 0.0.0.0:8000
