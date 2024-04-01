import heapq

def min_machines(start, end):
    if not start or not end or len(start) != len(end):
        return 0

    n = len(start)
    tasks = list(zip(start, end))
    tasks.sort(key=lambda x: x[0])  # Sort tasks by start times

    machines = []  # Use a min-heap to store machines by end times

    for task in tasks:
        current_start, current_end = task

        # Remove machines that have already finished by the current task's start time
        while machines and machines[0] <= current_start:
            heapq.heappop(machines)

        # Assign the task to the machine with the earliest end time or create a new machine
        if machines:
            heapq.heappop(machines)  # Remove the earliest-ending machine
        heapq.heappush(machines, current_end)  # Add the current task's end time to the heap

    return len(machines)

# Example usage:
start = [1, 8, 3, 9, 6]
end = [7, 9, 6, 14, 7]
print(min_machines(start, end))  # Output: 3
