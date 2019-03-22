# class parent():
#     c=0
#     def __init__(self):
#         self.context="mahmoud"
#     def get_obj_var(self):
#         parent.c=self.context
       
        
#     def a(self,b):
#         b=self.context
#         return b
#     b=a(self,b)
# b=0
# children= parent()
# c=children.get_obj_var()
# print(c)
# print(children.c)

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
        
    @classmethod    
    def set_date(cls,date):
        year,month,day=map(int,date.split('-'))
        return cls(year,month,day)
    @property
    def name(self):
        #making that name not accessed by the user even if it set it 
        self.var="default"
        return self.var

obj1=Date(1999,5,22)

obj1.var="ali"
obj1.mm="mmnn"
print(obj1.mm)
print (obj1.name)
print (obj1.var)
print(obj1.__dict__)
#obj2=Date.set_date("1999-5-22")

#print(obj1.year,obj2.year)
