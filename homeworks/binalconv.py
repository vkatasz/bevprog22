def conv(numb):
    hanyados=0
    maradek=""
    while numb>0:
        hanyados=int(numb/2)
        maradek+=str(numb%2)
        numb=hanyados
    return maradek

def main():
    ognumb=int(input("Enter a number: "))
    donecode=conv(ognumb)
    print("your entered number in binal code: {0}".format(donecode))

if __name__=="__main__":
    main()