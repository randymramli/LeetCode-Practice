def solution(A, B):
    print(sum([a!=b for a,b in zip(A,B)]))
    # return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2


if __name__ == '__main__':
    a= [1, 1, 4]
    b= [1, 2, 3]
    # a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
    # b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
    solution(a,b)