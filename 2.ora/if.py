def main():
    age=int(input('Age: '))

    if age>=18:
        print('Yes, you can')
    elif age==17:
        print('Almost, wait one more year :)')
    else:
        print('Nope')

if __name__=="__main__":
    main()