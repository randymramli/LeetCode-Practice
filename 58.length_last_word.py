def lengthOfLastWord(s):
    i = len(s) - 1
    print(i)
    count = 0

    while i >= 0 and s[i] == " ":
        i -= 1

    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1

    print(count)

if __name__ == "__main__":
    word = "luffy is still joyboy  "
    lengthOfLastWord(word)