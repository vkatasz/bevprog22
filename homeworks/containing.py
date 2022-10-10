from asyncio import windows_events


def chfinder(plntxt):
    const="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    matchingwds=""
    for wd in plntxt:
        for ws in const:
            if wd==ws:
                matchingwds+=wd
    return str(matchingwds)
    
def main():
    rndmstrng=input("Enter something: ")
    enteredinput=chfinder(rndmstrng)
    print("matching words: {0}".format(enteredinput))

if __name__=="__main__":
    main()