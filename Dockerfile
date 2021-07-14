FROM python:3

ADD . /

RUN pip install python-telegram-bot requests

CMD [ "python", "view.py" ]
