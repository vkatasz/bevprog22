from urllib.parse import non_hierarchical


def main():
    n1,n2=0,1
    nthterm,count=0,0
    nwanted=int(input("Which term do you want to see? "))
    if nwanted==0:
        print(n1)
    elif nwanted>0:
        print("A keresett érték: ")
        while count<nwanted:
            nthterm=n1
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
        print(nthterm)
    else:
        print("Please enter a positive intiger")

if __name__=="__main__":
    main()