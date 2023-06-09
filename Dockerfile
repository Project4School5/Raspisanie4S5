FROM python:3.8
WORKDIR /app

COPY . /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "bot.py"]
