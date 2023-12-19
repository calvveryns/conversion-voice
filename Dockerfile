FROM python:3.12.1
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade setuptools && pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]