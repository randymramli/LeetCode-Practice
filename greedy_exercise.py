def knapsack(content, W):
    n = len(content)
    content.sort(key=lambda x: round((x[0]/x[1]),2), reverse= True)

    final_value = 0

    for i in content:
        if i[1] <= W:
            W -= i[1]
            final_value += i[0]
        else:
            total_fraction = round(((i[0] * W) / i[1]),2)
            # print(total_fraction)
            final_value += total_fraction
    
    print(round(final_value,2))

class Job:
    def __init__(self,id,profit,deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline
    
    def __str__(self):
        return f'({self.id},{self.profit},{self.deadline})'

def job_sequencing(jobs):
    jobs.sort(key=lambda job: job.profit, reverse= True)
    # for job in jobs:
    #     print(job)
        
    max_deadline = 0

    for job in jobs:
        max_deadline = max(job.deadline,max_deadline)
    
    schedule = [-1] * (max_deadline + 1)
    total_profit = 0
    job_sequence = []

    for job in jobs:
        for t in range(job.deadline, 0, -1):
            if schedule[t] == -1:
                schedule[t] = job.id
                total_profit += job.profit
                job_sequence.append(job.id)
                break

    print(job_sequence, total_profit)
    print(schedule)

if __name__ == '__main__':
    # stuff = [[10,5],[5,3],[7,7],[6,1],[18,4],[9,1],[6,3],[7,5]]
    # max_w = 16
    # knapsack(stuff, max_w)

    jobs = [Job(1,9,2), Job(2,16,4), Job(3,10,1), Job(4,17,5), Job(5,13,2), Job(6,18,3)]
    job_sequencing(jobs)