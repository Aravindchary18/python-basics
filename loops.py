#this is about while loop this only executes the code only if the condition is true.
c=0
while c<9:

    print(c)
    c+=1
print("loop has ended")
#now we learn in list type
items=["age",56,"nine"]
for index,item in enumerate(items):
 print(index,item)
 #now we code about break and continue satements. in break code stops acc to the condition and in continue the code runs except the item mentioned in the condition.
items=[34,56,6,7]
for item in items:
   if item==6:
     break 
   print(item)