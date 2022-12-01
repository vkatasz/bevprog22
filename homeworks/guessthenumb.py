import random

def main():
    thenumb=random.randint(1,100)
    guessing=int(input("Guess a number: "))
    foundout=False
    while foundout==False:
        if thenumb!=guessing:
            guessing=int(input("Nope, try an other one: "))
        else:
            foundout=True
            print("DING DING DING, The answer is right!")

if __name__=="__main__":
    main()