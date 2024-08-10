# FROM python:3.12.4-bullseye
#
# WORKDIR /app
# COPY . /app 
# RUN pip install -r requirements.txt
#
# EXPOSE 8000
# CMD python ./server.py

FROM FROM alpine:3.14

WORKDIR /app
COPY . /app 

RUN apt update 
RUN 


