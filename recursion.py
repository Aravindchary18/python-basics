#n-1 → makes the function move toward stopping

#count_down(3) → starts the recursion

#return on top of print→ stops before printing 0

#recursion-

def recur(n):
    if n==0:
        return
    print(n)
    recur(n-1)

recur(3)
#by factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(4))