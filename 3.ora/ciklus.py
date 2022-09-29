def main():
    for x in range(1,15,2):
        print(x)

    print('\n')

    li=['répa','retek','karalábé']
    for word in li:
        print(word)

    print('\n')

    i=0
    while i<10:
        print(i)
        i+=1

    print('\n')

    i=0
    while True:
        print(i)
        i+=1
        if (i>4):
            break

if __name__=="__main__":
    main()