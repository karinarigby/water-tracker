FROM python:3.9.1

RUN pip install pipenv
ENV FLASK_APP run.py
COPY Pipfile /var/www/flask/
COPY Pipfile.lock /var/www/flask/

WORKDIR /var/www/flask
RUN pipenv install

COPY . .
CMD ["pipenv", "run", "gunicorn", "--config", "gunicorn_config.py", "--access-logfile", "-", "--error-logfile", "-", "wsgi:app"]