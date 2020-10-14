FROM python:3.7-slim

LABEL maintainer="TetszikABarCode"

RUN apt-get update

RUN pip3 install --upgrade pip && \
    pip3 install numpy pandas matplotlib scipy networkx EoN

VOLUME /project
WORKDIR /project