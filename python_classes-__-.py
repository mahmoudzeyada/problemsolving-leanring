class parent():
    c=0
    def __init__(self):
        self.context="mahmoud"
    def get_obj_var(self):
        parent.c=self.context
       
        
    def a(self,b):
        b=self.context
        return b
    b=a(self,b)
b=0
children= parent()
c=children.get_obj_var()
print(c)
print(children.c)