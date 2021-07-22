FROM ubuntu:14.04

RUN apt update
RUN apt install --no-install-recommends -y apt-utils wget xz-utils gcc-multilib autoconf make autotools-dev automake libboost-graph-dev g++

RUN apt-get update && \
    apt-get install --no-install-recommends -y ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libc6-dbg
RUN apt-get install -y libc6-dbg:i386

WORKDIR /
RUN wget --no-check-certificate https://www-users.cs.umn.edu/~smccaman/flowcheck/flowcheck-1.20.tar.xz
RUN tar xf flowcheck-1.20.tar.xz
WORKDIR flowcheck-1.20/valgrind-r15939+flowcheck
RUN ./autogen.sh
RUN ./configure --prefix=`pwd`/.. --enable-only32bit
RUN make -j4
RUN make install

WORKDIR /flowcheck-1.20/
COPY max-flow-boost.cc /flowcheck-1.20/max-flow-boost.cc
RUN g++ -O3 max-flow-boost.cc -o max-flow-boost

# copy benchmarks
WORKDIR /
COPY benchmarks /benchmarks 

WORKDIR /
RUN gcc -m32 benchmarks/test.c -I/flowcheck-1.20/include -o benchmarks/test
RUN head -100 /benchmarks/test.c >input
RUN gcc -m32 flowcheck-1.20/eg/wc.c -o /benchmarks/wc -I/flowcheck-1.20/include
RUN /benchmarks/wc input
RUN chmod o-r input
# RUN flowcheck-1.20/bin/valgrind --tool=exp-flowcheck --private-files-are-secret=yes /benchmarks/wc input

# RUN flowcheck-1.20/bin/valgrind --tool=exp-flowcheck --private-files-are-secret=yes --trace-secret-graph=yes --graph-file=/benchmarks/test.g --max-flow-program=/flowcheck-1.20/max-flow-boost /benchmarks/test 1
