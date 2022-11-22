FROM python:3.9-slim

RUN mkdir /app
COPY ./requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]