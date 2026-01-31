#Operator overloading means:
# Using operators (+, -, *, ==) on objects you create.
#Common operators you should know
#second value stores in operator method. and then comparisions get starts.
#Operator	Method
# +	__add__
# -	__sub__
# *	__mul__
# /	__truediv__
# ==	__eq__
# <	__lt__
# > __gt__
# we should definitely use this classes, because this doesnt know how to add objects(means def).
# normal use of operators 
print(2+3)
print("hi"+"bye")
#but this isnt go same for classes because it cant add two objects like this.
class addi:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def __gt__(self,fut):
          return True if self.age>fut.age else False
p1=addi("roger",26)
p2=addi("that",67)    
print(p1>p2)