FROM python:3.9

# Metadata indicating an image maintainer.
LABEL maintainer="manusenac@hotmail.com"

EXPOSE 8000
# Install pip requirements
WORKDIR /home

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install tk -y
RUN apt install fonts-noto pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev -y

RUN pip install poetry==1.1.11

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry update
RUN poetry install
RUN poetry lock

COPY screens/ screens/
COPY app/ app/
COPY main.py main.py
COPY planets.json planets.json
COPY setting.py setting.py
COPY utils.py utils.py

CMD python main.py