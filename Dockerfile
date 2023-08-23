FROM python:3.8.17-slim-bullseye

COPY . app/

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]