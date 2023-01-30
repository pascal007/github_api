FROM python:3.10-slim

RUN apt-get update -y \
    && apt-get install -y python3-pip gcc python3-dev musl-dev libffi-dev netcat

WORKDIR /app
COPY main/requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
COPY main /app

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["python", "manage.py", "run"]

