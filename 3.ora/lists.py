def main():
    numbone=['alma','répa','körte','bögre']
    numbtwo=['répa','retek','mogyoró','rigó']

    for word in numbone:
        if word in numbtwo:
            print(word)

if __name__=="__main__":
    main()