FROM ubuntu:22.04

WORKDIR /
COPY . /

RUN apt-get update -y && \
apt-get install python3 -y && \
apt-get install python3-pip -y

RUN chmod +x startup.sh
EXPOSE 8000
CMD [ "./startup.sh" ]