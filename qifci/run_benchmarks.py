import os

path = "/joana/ifc/sdg/qifc/joana.ifc.sdg.qifc.qif_interpreter"
exec_cmd = "time {cmd} ; "
run_cmd = path + "/run.sh {benchmark}"
pipe = "2> perf.txt > res.txt"


def run_qifci(benchmark_path, do_static):
    cmd = "{ " + exec_cmd.format(cmd=run_cmd.format(benchmark=benchmark_path)) + " } " + pipe
    os.system(cmd)

    with open(path + "/perf.txt", 'r') as perf:
        for line in perf.readlines():
            if "seconds time elapsed" in line:
                time = float((line.strip().split()[0].replace(',', '.')))

    dynLeak = "-"
    cc = "-"
    with open(path + "/res.txt", 'r') as res:
        for line in res.readlines():
            if "Channel capacity:" in line:
                cc = line.strip().split()[2]
            if "Dynamic Leakage:" in line:
                dynLeak = line.strip().split()[2]

    return time, cc, dynLeak


def avg(lst):
    return sum(lst) / len(lst)


def all_benchmarks(do_static):
    directory = "/benchmarks/"
    for f in os.listdir(directory):
        print(f)
        times = []
        for i in range(0, 10):
            time, cc, dynLeak = run_qifci(os.path.join(directory, f), do_static)
            times.append(time)
            print("Time: " + str(time) + " Channel Capacity: " + cc + " Dynamic Leak: " + dynLeak)
        print("Average: " + str(avg(times)))