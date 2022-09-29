from re import A


def main():
    a=int(input("add meg az a értéket: "))
    b=int(input("add meg a b értéket: "))

    while a!=b:
        if (a>b):
            a-=b
        else:
            b-=a
    print(a)

if __name__=="__main__":
    main()