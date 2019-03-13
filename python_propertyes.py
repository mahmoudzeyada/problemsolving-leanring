class c():
    def __init__(self,value=0):
        self.temp=value
    
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self,value):
        if value < -273 :
            raise ValueError("worng value")
        self.__temp=value

man=c()
man.temp=50000
print(man.temp)