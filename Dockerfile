FROM python:3.10-slim

RUN apt update -y && apt install awscli -y

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
