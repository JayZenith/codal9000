FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y build-essential python-psycopg2 && rm -rf /var/lib/apt/lists/*

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]