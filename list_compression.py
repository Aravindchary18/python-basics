#List comprehension = map() + filter() in one line
#List comprehension = a short way to create a list using a loop.

#without filtering modifing entire list. this is what map exactly does.

list=[6,8,7,9,53]
sqr=[n*n for n in list]
print(sqr)

#now with condition . this is what filter exactly does.
list=[2,3,4,5,6]
evens=[n for n in list if n%2==0]
print(evens)

#now using loops
list=[23,4,5,33]
loop=["evens are" if n%2==0 else "odd"for n in list]
print(loop)