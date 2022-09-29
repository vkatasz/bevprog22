def main():
    na=int(input("Natrium: "))
    cl=int(input("Chlorine: "))
    nacl=0
    excna=0
    exccl=0

    if cl==na:
        nacl=na
    
    elif cl>na:
        nacl=na
        excna=cl-na
    
    else:
        nacl=cl
        exccl=na-cl
    
    print("létrejött só: {0}\nmaradék nátriumatom: {1}\nmaradék klóratom: {2}".format(nacl,excna,exccl))

if __name__=="__main__":
    main()