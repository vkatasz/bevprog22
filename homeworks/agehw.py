def main():
    age=int(input("Age: "))

    if age>=21:
        print("You can drink alcohol in Amerika.")
    elif age>=18:
        print("You can buy tobacco product in Hungary, but you can't drink alcohol in Amerika")
    elif age>=16:
        print("You can get a driving licence in Amerika, but you can't drink alcohol and you can't buy tobacco product in Hungary")
    elif age>=12:
        print("You can watch Shrek 2, but you can't have a driving licence nor drink alcohol, nor get a driving licence, nor buy tobacco product in Hungary")
    else:
        print("You are too young, so get an icecream, and have a wonderful day :)")

if __name__=="__main__":
    main()