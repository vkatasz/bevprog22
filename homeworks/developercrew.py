class thecrew():

    def __init__(self,name,rank,inworky,salary):
        self.name=name
        self.rank="Junior"
        self.inworky=0
        self.salary=salary

    def salaryraise(self,salary):
        self.salary+=100000

    def inworkyear(self,inworky):
        self.inworky+=1

    def rankupgrade(self,inworky,rank):
        if self.inworky==0:
            self.rank="Intern"
        elif self.inworky>=1 and self.inworky<2:
            self.rank="Junior"
        elif self.inworky>2 and self.inworky<5:
            self.rank="Medior"
        else:
            self.rank="Senior"