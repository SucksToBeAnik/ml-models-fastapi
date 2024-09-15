FROM python:latest

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 80

CMD ["sh","-c","uvicorn main:app --host 0.0.0.0 --port 80"]