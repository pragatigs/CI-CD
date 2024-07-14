FROM python:3.9-slim-buster
WORKDIR .
# COPY ./requirements.txt /app
RUN pip install Flask
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]