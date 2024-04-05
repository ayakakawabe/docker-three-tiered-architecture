FROM python:3.11.9-slim-bullseye

RUN apt-get update && apt-get -y install && \
    groupadd -g 1100 pyuser && \
    useradd -m -s /bin/bash -u 1100 -g 1100 pyuser
