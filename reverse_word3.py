def reverse(s):
    new = s.split(" ")
    update = []
    for i in new:
        i = i[::-1]
        update.append(i)
    print(" ".join(update))


def main():
    word = "Let's take LeetCode contest"
    reverse(word)


main()