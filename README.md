# Evaluation Setup for different QIF Tools

Used for the evaluation in my thesis: [``https://github.com/tnstrssnr/thesis``](https://github.com/tnstrssnr/thesis)

## Tools
The evaluation includes the following tools:
- QIFCI [``https://github.com/tnstrssnr/joana``](https://github.com/tnstrssnr/joana)
- Nildumu  [``https://github.com/parttimenerd/nildumu``](https://github.com/parttimenerd/nildumu)
- ApproxFlow [``https://github.com/parttimenerd/approxflow``](https://github.com/parttimenerd/approxflow)
    (adapted version that includes a newer version of approxmc, the original applicationcan be found at [``https://github.com/approxflow/approxflow``](https://github.com/approxflow/approxflow)
- Flowcheck [``https://www-users.cse.umn.edu/~smccaman/flowcheck/``](https://www-users.cse.umn.edu/~smccaman/flowcheck/)

## Benchmarks
The benchmark programs were translated into the programming language required by the tools. Apart from this, there are no semantic differences between the benchmark programs in each directory.

## Setup
For each tool, we provide a separate Docker image along with a set of benchmark programs and a script to run the benchmarks in different configurations.

To run the benchmarks, build the Docker container from the provided ``Dockerfile`` and then run the container.

## Evaluation Setup
Each Docker container will run the benchmark programs using different tool configurations. The benchmark script will run each benchmark 10 times and print the execution time and the calculated information leakage for each run. After all 10 runs ofa benchmark program are completed, the average run time is reported.

**ApproxFlow**:
Each benchmark is run twice:
- Once with UNWIND set to 8
- Once with UNWIND set to 32

**Nildumu**:
Each benchmark is run twice:
- Once with an inlining bound of 8
- Once with an inlining bound of 32