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
Each Docker container will run the benchmark programs using different tool configurations. A benchmark run consists of 10 executions of the benchmark program. For each execution the script will print the execution time and the calculated information leakage. After all 10 executions are completed, the average run time is reported.

### **ApproxFlow**:
Each benchmark is run twice:
- Once with UNWIND set to 8
- Once with UNWIND set to 32

### **Nildumu**:
Each benchmark is run twice:
- Once with an inlining bound of 8
- Once with an inlining bound of 32

### **Flowcheck**: *under construction*
Using the min-cut algorithm in Flowcheck currently doesn't work. The benchmarks are run one, with using min-cut.

The input values that are used to test the benchmarks are annotated as comments in the benchmark source code.
More arguments can be added in separate comments, the script will execute them automatically.

### **QIFCI**:

Channel capacity analysis - Configurations:
1. no pre-processing, no hybrid analysis
2. pre-processing, no hybrid analysis
3. pre-processing and hybrid analysis

For each configuration, each benchmark is run twice:
- Once with an iteration / recursion bound of 8
- Once with an iteration / recursion bound of 32

Dynamic Leakage analysis - Configuration: no pre-processing, no hybrid analysis

The input values that are used to test the benchmarks are annotated as comments in the benchmark source code.
More arguments can be added in separate comments, the script will execute them automatically.

For each set of input values, the benchmark is run twice:
- Once with an iteration / recursion bound of 8
- Once with an iteration / recursion bound of 32

*Note:* The ``SumQuery`` benchmark is currently omitted from the dynamic leakage analysis as it can lead to time-outs.