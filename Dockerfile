FROM python:3.10.8

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn
VOLUME db.sqlite3
RUN python3 manage.py makemigrations &&\
    python3 manage.py migrate &&\
    python3 manage.py collectstatic --noinput

CMD ["gunicorn", "MovieCollection.wsgi", "--bind=unix:/var/run/gunicorn/gunicorn.sock"]