FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install --trusted-host pypi.python.org --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3","-m","WebStreamer"]
