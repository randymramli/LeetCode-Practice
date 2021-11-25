def string_dif(a,b):
    a = list(a)
    b = list(b)
    for i in a:
        b.remove(i)
    print(b)

def string_dif2(a,b):
    ch = 0
    for i in a:
        print(str(i) + "=" + str(ord(i)))
        ch ^= ord(i)
        print(ch)
    
    for j in b:
        print(str(j) + "=" + str(ord(j)))
        ch ^= ord(j)
        print(ch)


def main():
    word = "ae"
    word2 = "aea"
    string_dif(word,word2)
    string_dif2(word,word2)

main()