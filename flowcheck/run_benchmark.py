import os
import subprocess
import sys

exec_cmd = "time {cmd} ; "
flowcheck_cmd = "./check.sh {benchmark} {o} {args}"
pipe = "2> perf.txt > res.txt'"

def run_flowcheck(benchmark_path, benchmark_name, args):

    cmd = "/bin/bash -c '{ " + exec_cmd.format(cmd=flowcheck_cmd.format(benchmark=benchmark_path, benchmark_name=benchmark_name, args=args)) + " } " + pipe
    subprocess.call(cmd, shell=True)

    with open("perf.txt", 'r') as perf:
        for line in perf.readlines():
            if "real" in line:
                time = (line.strip().split()[1])
                time = time.split('m')[1]
                time = float(time[:-1])
    
    leak = None
    with open("res.txt", 'r') as res:
        for line in res.readlines():
            if "Leaked" in line:
                leak = line.strip().split()[1]
    return time, leak

def avg(lst):
    return sum(lst) / len(lst)

def all_benchmarks():
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        print("-----------------------------------------")
        print("Program: " + f)
        times = []
        for i in range(0, 10):
            time, leak = run_flowcheck(os.path.join(directory, f), f, 0)
            os.system("./clean.sh")
            if leak == None:
                leak = "run failed"
                time = 0
            times.append(time)
            print("Time: " + str(time) + " Leak: " + leak)
        
        print("Average: " + str(avg(times)))

def run_config(bound):
    print("*****************************************")
    all_benchmarks()
    print("*****************************************")

run_config(8)
run_config(32)