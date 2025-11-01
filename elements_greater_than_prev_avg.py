def countResponseTimeRegressions(responseTimes):
    # Write your code here
    result = 0
    
    n = len(responseTimes)
    if n < 2:
        print(result)
    
    total= responseTimes[0]

    for i in range(1,n):
        avg = total / i
        if responseTimes[i] > avg:
            result += 1
        total += responseTimes[i]
    print(result)

if __name__ == "__main__":
    a = [100,200,150,300]
    countResponseTimeRegressions(a)