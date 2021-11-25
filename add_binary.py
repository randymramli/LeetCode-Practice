def binary(a, b):
    a = int(a,2)
    b = int(b,2)
    c = a + b
    new = "{0:b}".format(c)
    print(new)

def main():
    a = "11"
    b = "1"
    binary(a,b)


main()