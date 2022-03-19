def majorityElement(x):
    count = 0
    candidate = None

    for i in x:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    print(candidate)

def main():
    nums = [7,7,7,8,9,2,7]
    majorityElement(nums)

main()