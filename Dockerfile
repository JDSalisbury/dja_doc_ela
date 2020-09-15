FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server
RUN pip install -r requirements.txt