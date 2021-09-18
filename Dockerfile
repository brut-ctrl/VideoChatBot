FROM python:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN apt -qq install -y --no-install-recommends git
COPY . /VideoChatBot
WORKDIR /VideoChatBot
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt
CMD python3 -m bot
