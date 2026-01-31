#A docstring is a string written inside a function to explain what it does.
#here's a simple example
# simple code
def func(a,b):
    """this function adds two numbers"""
    return a+b
print(func(5,5))
help(func)

#Annotations
#Annotations tell what type of data a function expects and returns.
#They do NOT change how the code runs — only for understanding.
def anno(a:int,b:int)-> int:
    return a+b

print(anno(2,3))
help(anno)
print(anno.__annotations__)