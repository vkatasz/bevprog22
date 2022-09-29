def main():
    num=int(input("Enter a number: "))
    reversed=int(str(num)[::-1])
    if num==reversed:
        print("Yey, mirrornumber :D")
    else:
        print("No, it's not :(")

if __name__=="__main__":
    main()