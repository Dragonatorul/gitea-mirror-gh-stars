FROM python:3.11-slim

ENV USER=app
ENV UID=1000
ENV GID=1000

COPY src/main.py /app/main.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    pip install --no-cache-dir --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove gcc build-essential && \
    rm -rf /var/lib/apt/lists/* /root/.cache/pip /tmp/*

RUN groupadd -g ${GID} ${USER} && \
    useradd -u ${UID} -g ${GID} -s /bin/bash -m ${USER}

USER ${USER}

CMD [ "python3", "main.py"]