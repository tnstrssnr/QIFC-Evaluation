FROM ubuntu:20.04

LABEL maintainer="stroessner.tinamaria@gmail.com"
LABEL version="0.1"

ARG DEBIAN_FRONTEND=noninteractive

# based on Dockerfile in https://github.com/parttimenerd/nildumu

RUN apt update
RUN apt-get update -y
RUN apt-get install -y git maven vim nano gcc g++ wget unzip python pip

# Install OpenJDK-8     # see: https://stackoverflow.com/a/44058196
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /
RUN git clone https://github.com/parttimenerd/nildumu.git

WORKDIR /nildumu
RUN ./download_solvers
RUN mvn compile -DskipTests
RUN mvn package -DskipTests

WORKDIR / 
COPY benchmarks/ /benchmarks

WORKDIR /
COPY run_benchmark.py /run_benchmark.py

WORKDIR /
CMD python3 run_benchmark.py
