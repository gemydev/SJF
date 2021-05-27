# from code.sjf_preemptive import*

from sjf_preemptive import find_avg_time

if __name__ == "__main__":
    # Process id's
    # list of [Process Num , Burst Time , Arrival Time ]
    actual_processes = [[2, 12, 0], [3, 8, 3],
                        [4, 4, 5], [1, 10, 10], [5, 6, 12]]
    # n => Number of precesses
    n = 5
    find_avg_time(actual_processes, n)
