FROM golang:1.11.5

ENV APP_NAME app
ENV PORT 8080

#RUN wget 'http://www.gutenberg.org/files/2600/2600-0.txt' -O war_and_peace.txt

COPY . /go/src/${APP_NAME}
WORKDIR /go/src/${APP_NAME}

RUN go get ./
RUN go build -o ${APP_NAME}

CMD ./${APP_NAME}

EXPOSE ${PORT}

