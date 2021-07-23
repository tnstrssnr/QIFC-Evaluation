import os
import subprocess

exec_cmd = "time {cmd} "
approxflow_cmd = "./run {benchmark}"
args = "--handler=inlining;maxrec={bound};bot=summary"
pipe = "2> perf.txt > res.txt'"

def run_nildumu(benchmark_path, bound):

    cmd = "/bin/bash -c '{ " + exec_cmd.format(cmd=approxflow_cmd.format(benchmark=benchmark_path)) + " " + args.format(bound=str(bound)) + " ; } " + pipe
    subprocess.call("cd nildumu && " + cmd, shell=True)

    with open("/nildumu/perf.txt", 'r') as perf:
        for line in perf.readlines():
            if "real" in line:
                time = (line.strip().split()[1])
                time = time.split('m')[1]
                time = float(time[:-1])
    
    leak = None
    with open("/nildumu/res.txt", 'r') as res:
        for line in res.readlines():
            if "Leakage: " in line:
                leak = line.strip().split()[1]
    return time, leak

def avg(lst):
    return sum(lst) / len(lst)

def all_benchmarks(bound):
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        print(f)
        times = []
        for i in range(0, 10):
            time, leak = run_nildumu(os.path.join(directory, f), bound)
            if leak == None:
                leak = "run failed"
                time = 0
            times.append(time)
            print("Time: " + str(time) + " Leak: " + leak)
        print("Average: " + str(avg(times)))
        
def run_config(bound):
    print("*****************************************")
    print("Using unwinding bound: " + str(bound))
    all_benchmarks(bound)
    print("*****************************************")

run_config(8)
run_config(32)