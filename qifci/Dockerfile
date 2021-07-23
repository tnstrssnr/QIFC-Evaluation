FROM ubuntu:20.04

LABEL maintainer="stroessner.tinamaria@gmail.com"
LABEL version="0.1"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt-get update -y
RUN apt-get install -y git maven vim nano gcc g++ wget unzip python pip ant build-essential cmake zlib1g-dev libboost-program-options-dev libm4ri-dev

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# setup joana base
WORKDIR /
RUN git clone https://github.com/tnstrssnr/joana.git

WORKDIR /joana/
RUN git submodule init
RUN git submodule update
RUN ./setup_deps

# install approxmc + cryptominisat
RUN apt-get install -y libgmp10 libgmp-dev
WORKDIR /joana/ifc/sdg/qifc/joana.ifc.sdg.qifc.qif_interpreter
RUN ./setup.sh

WORKDIR /joana/ifc/sdg/qifc/joana.ifc.sdg.qifc.qif_interpreter
RUN ant

WORKDIR / 
COPY benchmarks/ /benchmarks

RUN /joana/ifc/sdg/qifc/joana.ifc.sdg.qifc.qif_interpreter/run.sh /benchmarks/SumQuery.java --static

WORKDIR /
COPY run_benchmark.py /run_benchmark.py