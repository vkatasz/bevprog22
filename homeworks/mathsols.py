def main():
    sin=0
    cos=0
    tg=0
    inp=input("add meg melyik függvényt szeretnéd kiszámolni, sin, cos, vagy tg: ")

    if inp=="sin":
        b=int(input("add meg az 'b' oldal értékét: "))
        c=int(input("add meg a 'c' oldal értékét: "))
        sin=b/c
        print(sin)
    elif inp=="cos":
        a=int(input("add meg az 'a' oldal értékét: "))
        c=int(input("add meg a 'c' oldal értékét: "))
        cos=a/c
        print(cos)
    elif inp=="tg":
        b=int(input("add meg a 'b' oldal értékét: "))
        a=int(input("add meg az 'a' oldal értékét: "))
        tg=b/a
        print(tg)
    else:
        print("érvnyktelen függvény.")
    

if __name__=="__main__":
    main()