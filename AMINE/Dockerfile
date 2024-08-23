FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=AMINE.settings

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "AMINE.wsgi:application"]
