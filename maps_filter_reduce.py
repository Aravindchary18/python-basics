#maps,filter,reduce modifies lists.
#these have parenthesis at the end.
#maps used to convert whole list . every item in the list acc to the condition given by the user.
#filter takes a list , keeps item only if it matches the condition . 
#reduce takes a list, combines all values. that is we get only one value in the end.note-reduce is not built in , you must import it.
#must have 2 arguments in the maps,filter,reduce. like ex lambda condition , variable of list. 

#maps-

nums=[3,4,2,1]
ans=list((map(lambda a:a%2,nums)))
print(ans)

#filter-

nums=[20,10,50,2]
ans=list(filter(lambda a:a%10==0,nums))
print(ans)

#reduce-

from functools import reduce
nums=[1,2,3,4,5]
ans=reduce(lambda a,b:a+b,nums)
print(ans)