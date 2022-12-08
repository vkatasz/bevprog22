def main():
    reader = open("pivers.txt",'r')
    vers = str(reader.readline()).split(sep=" ")
    reader.close

    reader = open("pinum.txt","w")
    for x in vers:
        print(len(x),end="", file=reader)
        if(x == vers[0]):
            print(".",end="", file=reader)
    reader.close

if __name__ == "__main__":
    main()