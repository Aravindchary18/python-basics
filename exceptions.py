#we use try and exceptions so the program doesnt crash.print.print.print.
#try must be followed by except or finally
#More specific exceptions first

try:
    x=10/0
    print(x)

except:
    print("error happened")

# rasing exceptions manually ( sokmewhat intermediate level)

try:
    
    age=int(input("enter the age:"))
    if age<18:
         raise ValueError("age must be grater than 18")
except ValueError as e :
    print(e)

# now opening a file. this runs whether exceptions occurs or not

try:
    f=open("aravind.py")
    print("file opened")
except FileNotFoundError:
    print("unknown file")
finally:
    if 'f' in locals():
        f.close()
    print("cleanup done")
# we can this above code much easier with "with concept"

import os
print(os.getcwd())

try:
    with open("exceptions.py") as f:
        print(f.read())
        print("file opened succeddfully")
except FileNotFoundError:
    print("file not found")