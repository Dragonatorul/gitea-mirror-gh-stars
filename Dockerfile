FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV USER=app
ENV UID=1000
ENV GID=1000

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY src/main.py /app/main.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    rm -rf /tmp/*

RUN groupadd -g ${GID} ${USER} && \
    useradd -u ${UID} -g ${GID} -s /bin/bash -m ${USER}

USER ${USER}

CMD [ "python3", "main.py"]