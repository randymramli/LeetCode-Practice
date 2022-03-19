def average(salary):
        return (sum(salary) - min(salary) - max(salary)) / float(len(salary) - 2)

if __name__ == '__main__':
        salary = [4000,3000,1000,2000]
        average(salary)