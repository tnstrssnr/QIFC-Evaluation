FROM ubuntu:20.04

LABEL maintainer="stroessner.tinamaria@gmail.com"
LABEL version="0.1"

ARG DEBIAN_FRONTEND=noninteractive


RUN apt update
RUN apt-get update -y

# installing some basic stuff
RUN apt-get install -y autoconf automake libtool make cmake pip gcc git g++ maven python2 python-pycparser build-essential zlib1g-dev libboost-program-options-dev libm4ri-dev libsqlite3-dev help2man linux-tools-common linux-tools-generic python3


# installing dependencies needed for approxflow
RUN apt-get install -y tcc cbmc wget
RUN pip install subprocess32

WORKDIR /
RUN wget https://github.com/msoos/cryptominisat/archive/5.8.0.tar.gz
RUN tar -xvf 5.8.0.tar.gz
WORKDIR /cryptominisat-5.8.0
RUN mkdir build
WORKDIR /cryptominisat-5.8.0/build
RUN cmake ..
RUN make -j6 && make install
RUN ldconfig

WORKDIR /
RUN git clone https://github.com/parttimenerd/approxflow.git

WORKDIR /
COPY benchmarks /benchmarks
COPY clean.sh /clean.sh
RUN chmod +x clean.sh

COPY run_benchmark.py /run_benchmark.py

CMD python3 run_benchmark.py
