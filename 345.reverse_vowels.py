def reverseVowels(s):
    vowels = "aiueoAIUEO"
    word = list(s)
    start = 0
    end = len(word) -1

    while start < end:
        while start < end and vowels.find(word[start]) == -1:
            start += 1
        
        while start < end and vowels.find(word[end]) == -1:
            end -= 1
        
        word[start], word[end] = word[end], word[start]

        start += 1
        end -= 1

    a = "".join(word)

    print(a)


if __name__ == '__main__':
    a = "hello"
    b = "leetcode"
    reverseVowels(a)
    reverseVowels(b)
