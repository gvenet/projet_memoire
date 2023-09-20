FROM python:3.9
WORKDIR /app
COPY ./requirements.prod.txt .
RUN pip install -r requirements.prod.txt
COPY . .
EXPOSE 5001
