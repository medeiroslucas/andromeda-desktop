FROM ubuntu:latest

# Metadata indicating an image maintainer.
LABEL maintainer="manusenac@hotmail.com"
ENV DEBIAN_FRONTEND=noninteractive
EXPOSE 8000
# Install pip requirements
WORKDIR /home
COPY requirements.txt .
RUN apt-get update && apt-get upgrade
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN python3 -m pip install -r requirements.txt
RUN apt install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev -y
RUN python3 -m pip install poetry 




# Sets a command or process 
#that will run each time a container is run from the new image.


