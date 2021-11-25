def majorityElement(x):
    new_dict = {}
    for i in x:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    v = list(new_dict.values())
    k = list(new_dict.keys())
    a = max(v)
    b = v.index(a)
    c = k[b]
    print(c)

def main():
    nums = [3,2,3,1,8,5,6,7,4,5,4,9,4,6,8,9,1,2,1,1,1,3]
    majorityElement(nums)

main()