FROM python:latest
COPY requirements.txt /usr/src/code/
WORKDIR /usr/src/code
RUN pip3 install -r requirements.txt
COPY . /usr/src/code/
CMD python3 periodic_service.py