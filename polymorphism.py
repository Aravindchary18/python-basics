#polymorphism
#methos names are nothing the nmaes that comes after def
#Different method names → no polymorphism.


#can use Same function, different types like below code .

print(len("hell and heaven"))
print(len((1,2,3)))
print(9+9)
print("hi"+"bye")
# now method overrriding (oop)
class animal:
    def eats(self):
        print("animal")
class dog:
    def eats(self):
        print("dog eats")
class human:
    def eats(self):
        print("human does wrok")
ah=[dog(),human(),animal()]
for a in ah:
    a.eats()