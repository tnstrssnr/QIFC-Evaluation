import os

exec_cmd = "time {cmd} ; "
approxflow_cmd = "python2 ApproxFlow.py {benchmark} f"
pipe = "2> perf.txt > res.txt'"

def run_approxflow(benchmark_path):

    cmd = "/bin/bash -c '{ " + exec_cmd.format(cmd=approxflow_cmd.format(benchmark=benchmark_path)) + " } " + pipe

    os.system("cd approxflow && " + cmd)

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
        print(f)
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
        

all_af_benchmarks()