class theline():

    def __init__(self):
        self.theline=""

    def addedend(self,num):
        self.theline+=str(num)+" "
    
    def devidedend(self):
        if self.theline=="":
            return None
        line=self.theline.split(" ")
        for i in range(1,len(line)-1):
            self.theline+=line[i]+" "
        return int(line[0])

    def size(self):
        return len(self.theline.split(" "))-1

    def empty(self):
        if self.theline=="":
            return True
        else:
            return False

    def __str__(self):
        return "["+self.theline

def main():
    line=theline()
    print(line)
    print(line.empty())
    line.addedend(1)
    line.addedend(4)
    line.addedend(5)
    print(line)
    print(line.size())
    print(line.empty())
    out=line.devidedend()
    print(out)
    print(line)
    line.devidedend()
    line.devidedend()
    out=line.devidedend()
    print(out)

if __name__=="__main__":
    main()