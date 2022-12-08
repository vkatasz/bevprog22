def diff(a,b):
    if a>b:
        return a-b
    if b>a:
        return b-a
    return 0

def main():
    skyscrapers=[ord(n) for n in str(2**1024)]
    sumdiff=0
    i=0
    while i<len(skyscrapers)-1:
        sumdiff+=diff(skyscrapers[i],skyscrapers[i+1])
        i+=1
    print(sumdiff)

if __name__=="__main__":
    main()