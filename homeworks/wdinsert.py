def main():
    wdno1=input("Adj meg egy mondatot: ")
    wdno2=input("Adj meg egy szót amit a mondatba szeretnél beilleszteni: ")
    wdplace=input("Add meg melyik szó elé szeretnéd beilleszteni: ")

    ind=wdno1.find(wdplace)
    outp=wdno1[:ind]+wdno2+" "+wdno1[ind:]
    print(outp)

if __name__=="__main__":
    main()