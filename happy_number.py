def happy_number(x):
    if x == 1:
        print("True")
    a = []
    for i in str(x):
        a.append(int(i)**2)
    b = sum(a)
    print(a)
    if b == 1:
        print("True")
    else:
        happy_number(sum(a))


def main():
    happy_number(19)



main()