FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY ./requiremets.txt /app/requirements.txt
RUN pip install -r requiremets.txt
COPY . /app
