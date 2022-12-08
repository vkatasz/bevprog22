def main():

    red = open("string1.py", 'r')
    rit = open('clean.py','w')
    writ = open('clean2.py','w')
    
    lis = red.readline()
    while(lis):
        if not lis.startswith('#'):
            print(lis, end="", file=rit)
            if not lis.find('#')>-1:
                print(lis, end="", file=writ)
        lis = red.readline()

    red.close
    rit.close
    writ.close

if __name__ == "__main__":
    main()