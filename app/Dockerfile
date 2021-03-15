
# build stage
FROM golang as builder

ENV GO111MODULE=on

WORKDIR /code

COPY go.mod /code/

RUN wget 'http://www.gutenberg.org/files/2600/2600-0.txt' -O /code/war_and_peace.txt
#RUN mv war_and_peace.txt /code/

RUN go mod download

COPY . /code/

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

# final stage
FROM scratch
COPY --from=builder /code/app /code/
EXPOSE 8080
ENTRYPOINT ["/code/app"]