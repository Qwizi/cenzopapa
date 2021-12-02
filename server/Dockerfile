FROM python:3
RUN mkdir /project
WORKDIR /project

RUN apt-get install build-essential libssl-dev libffi-dev python3-dev cargo

COPY requirements.txt /project/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /project/
RUN chmod +x entrypoint.prod.sh

ENTRYPOINT ["bash", "entrypoint.prod.sh" ]