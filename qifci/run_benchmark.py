import os
import subprocess

path = "/joana/ifc/sdg/qifc/joana.ifc.sdg.qifc.qif_interpreter"
exec_cmd = "time {cmd} "
run_cmd = path + "/run.sh {benchmark}"
pipe = "2> perf.txt > res.txt'"


def run_qifci(benchmark_path, args):
    cmd = "/bin/bash -c '{ " + exec_cmd.format(cmd=run_cmd.format(benchmark=benchmark_path)) + args + " ; } " + pipe
    subprocess.call(cmd, shell=True)

    with open("perf.txt", 'r') as perf:
        for line in perf.readlines():
            if "real" in line:
                time = (line.strip().split()[1])
                time = time.split('m')[1]
                time = float(time[:-1])

    dynLeak = "-"
    cc = "-"
    with open("res.txt", 'r') as res:
        for line in res.readlines():
            if "Channel capacity:" in line:
                cc = line.strip().split()[2]
            if "Dynamic Leakage:" in line:
                dynLeak = line.strip().split()[2]
    
    remove_output_dirs()

    return time, cc, dynLeak


def avg(lst):
    return sum(lst) / len(lst)


def all_benchmarks(args):
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        print(f + " " + args)
        times = []
        for i in range(0, 10):
            time, cc, dynLeak = run_qifci(os.path.join(directory, f), args)
            times.append(time)
            print("Time: " + str(time) + " Channel Capacity: " + cc + " Dynamic Leak: " + dynLeak)
        print("Average: " + str(avg(times)))


def static_args(bound, pp, hybrid):
    args = " --static"
    if pp:
        args += " --pp"
    if hybrid:
        assert(pp)
        args += " --hybrid"
    args += " --unwind " + str(bound)
    return args


def run_static_config(bound, pp, hybrid):
    print("*****************************************")
    print("Running only channel capacity analysis")
    print("Using unwinding bound: " + str(bound))
    if pp:
        print("Pre-Processing enabled")
    if hybrid:
        print("Hybrid analysis enabled")
    all_benchmarks(static_args(bound, pp, hybrid))
    print("*****************************************")


def run_dyn(benchmark_path, bound):
    args = []
    with open(benchmark_path, 'r') as f:
        for line in f.readlines():
            if "//" in line:
                arg = line.strip().split()[1:]
                args.append("--args " + " ".join(arg))
    
    for arg in args:
        print(benchmark_path + " " + arg)
        times = []
        for i in range(0, 10):
            time, cc, dynLeak = run_qifci(benchmark_path, arg)
            times.append(time)
            print("Time: " + str(time) + " Channel Capacity: " + cc + " Dynamic Leak: " + dynLeak)
        print("Average: " + str(avg(times)))


def run_all_dyn(bound):
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        run_dyn(os.path.join(directory, f), bound)


def run_dyn_config(bound):
    print("*****************************************")
    print("Analysing channel capacity + Dynamic Leakage")
    print("Hybrid analysis disabled")
    all_benchmarks(run_all_dyn(bound))
    print("*****************************************")

def remove_output_dirs():
    out_dirs =  path + "/out_*"
    cmd = "rm -r " + out_dirs
    subprocess.call(cmd)

run_dyn_config(8)
run_dyn_config(32)
