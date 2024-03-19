def solution(s):
    size = 256
    freq = [0] * size
    for i in range(len(s)):
        freq[ord(s[i])] += 1
    odd_count = 0
    for i in freq:
        if (i % 2) != 0:
            odd_count += 1
    if odd_count > 1:
        return False
    return True

if __name__ == '__main__':
    s = "aarcrce"
    solution(s)