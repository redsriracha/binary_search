FROM ubuntu

WORKDIR /app
COPY *.py /app

RUN apt update
RUN apt install -y python3

# RUN apt install -y python3-pip
# COPY requirements.txt /tmp
# RUN python3 -m pip install -r /tmp/requirements.txt
# RUN rm /tmp/requirements.txt