import os
import subprocess
import sys

exec_cmd = "time {cmd} ; "
approxflow_cmd = "python2 ApproxFlow.py {benchmark} f"
pipe = "2> perf.txt > res.txt'"

def run_approxflow(benchmark_path):

    cmd = "/bin/bash -c '{ " + exec_cmd.format(cmd=approxflow_cmd.format(benchmark=benchmark_path)) + " } " + pipe
    subprocess.call("cd approxflow && " + cmd, shell=True)

    with open("/approxflow/perf.txt", 'r') as perf:
        for line in perf.readlines():
            if "real" in line:
                time = (line.strip().split()[1])
                time = time.split('m')[1]
                time = float(time[:-1])
    
    leak = None
    with open("/approxflow/res.txt", 'r') as res:
        for line in res.readlines():
            if "f : " in line:
                leak = line.strip().split()[2]
    return time, leak

def avg(lst):
    return sum(lst) / len(lst)

def all_af_benchmarks():
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        print("-----------------------------------------")
        print("Program: " + f)
        times = []
        for i in range(0, 10):
            time, leak = run_approxflow(os.path.join(directory, f))
            os.system("./clean.sh")
            if leak == None:
                leak = "run failed"
                time = 0
            times.append(time)
            print("Time: " + str(time) + " Leak: " + leak)
        
        print("Average: " + str(avg(times)))
        
def set_unwind(bound):
    os.environ['UNWIND'] = str(bound)

def run_config(bound):
    print("*****************************************")
    print("Using unwinding bound: " + str(bound))
    all_af_benchmarks()
    print("*****************************************")

run_config(8)
run_config(32)