def find_waiting_time(processes, n, wt):
    burst_times = [0] * n

    for i in range(n):
        burst_times[i] = processes[i][1]
    complete = 0
    t = 0
    minimum = 999999999
    short = 0
    check = False

    # Process until all processes gets
    # completed
    while complete != n:

        # Find process with minimum remaining
        # time among the processes that
        # arrives till the current time`
        for j in range(n):
            # if arrival time at [j] less than t &&
            # burst_times at [j] less than minimum &&
            # burst_times at [j] more than 0
            if (processes[j][2] <= t) and (burst_times[j] < minimum) and burst_times[j] > 0:
                minimum = burst_times[j]
                short = j
                check = True

        if not check:
            t += 1
            continue

        # Reduce remaining time by one
        burst_times[short] -= 1

        # Update minimum
        minimum = burst_times[short]
        if minimum == 0:
            minimum = 999999999

        # If a process gets completely
        # executed
        if burst_times[short] == 0:

            # Increment complete
            complete += 1
            check = False

            finish_time_of_current_process = t + 1

            # Calculate waiting time
            wt[short] = (finish_time_of_current_process - actual_processes[short][1] -
                         actual_processes[short][2])

            if wt[short] < 0:
                wt[short] = 0

        # Increment time
        t += 1


# Function to calculate turn around time
def find_turn_around_time(processes, n, wt, tat):
    # Calculating turnaround time
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]

    # Function to calculate average waiting


# and turn-around times.
def find_avg_time(processes, n):
    waiting_time = [0] * n
    turn_around_time = [0] * n

    # Function to find waiting time
    # of all processes
    find_waiting_time(processes, n, waiting_time)

    # Function to find turn around time
    # for all processes
    find_turn_around_time(processes, n, waiting_time, turn_around_time)

    # Display processes along with all details
    print("Processes    Burst Time     Waiting", "Time     Turn-Around Time")
    total_waiting_time = 0
    total_around_time = 0
    for i in range(n):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_around_time = total_around_time + turn_around_time[i]
        print(" ", processes[i][0], "\t\t",
              processes[i][1], "\t\t\t\t",
              waiting_time[i], "\t\t\t\t", turn_around_time[i])

    print("\nAverage waiting time = %.5f " % (total_waiting_time / n))
    print("Average turn around time = ", total_around_time / n)


# Driver code
if __name__ == "__main__":
    # Process id's
    # list of [Process Num , Burst Time , Arrival Time ]
    actual_processes = [[1, 6, 1], [2, 8, 1],
                        [3, 7, 2], [4, 3, 3]]
    # n => Number of precesses
    n = 4
    find_avg_time(actual_processes, n)
