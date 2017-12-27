class ClassA:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def cPrint(self):
        print("Hello ClassA")
    
    def add(self) -> object:
        print("x和y的和为：%d"%(self.x+self.y))