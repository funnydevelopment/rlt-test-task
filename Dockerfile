FROM ubuntu:latest
LABEL authors="chayan"

ENTRYPOINT ["top", "-b"]