FROM python:3.8-buster
COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
