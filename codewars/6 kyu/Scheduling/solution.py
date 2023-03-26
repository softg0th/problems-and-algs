def SJF(jobs, index):
    sum = 0
    for i in range(len(jobs)):
        if jobs.index(min(jobs)) == index:
            return sum+min(jobs)
        el = min(jobs)
        sum += el
        tag = jobs.index(el)
        jobs[tag] = max(jobs) + 2


print(SJF([3,10,20,1,2], 1))