def length(s):
    a =len(s.rstrip().split(" ")[-1])
    b = s.rstrip().split(" ")
    print(a)
    print(b)

def main():
    word = "Hello world"
    word2 = "a "
    length(word)
    length(word2)


main()