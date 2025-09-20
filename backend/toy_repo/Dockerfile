FROM python:3.7

ENV PYTHONPATH=/usr/local/lib/python/3.7/site-packages:/etc/security/bashrc:/etc/profile/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/sbin:/root/bin:/usr/lib/x86_64-linux-gnu:/opt/webapp/bin

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

RUN apt-get update && \
    apt-get install --no-cache-dir build-essential \
    python-bcrypt python-jose python-dateutil python-postgresql python-psycopg2 python-virtualenv \
    python-dotenv

COPY . /app/

RUN rm -rf /var/lib/flask/