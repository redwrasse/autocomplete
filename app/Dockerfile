FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt /code/
RUN wget 'http://www.gutenberg.org/files/2600/2600-0.txt' -O war_and_peace.txt
RUN mv war_and_peace.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV FLASK_APP app.py
CMD flask run --host=0.0.0.0

