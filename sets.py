#sets are similar has list,tuples,dictionaries.These form list with curved brackets.this is like a combination of list and dictionaries.
#note- sets dont repeat same items in the list it removes the extra word and keeps only one from them.
set1={"gone","stoneage","boy","gone"}
set2={"stoneage"}
intersect=set1&set2
print(intersect)
mod=set1|set2
mod2=set1<set2
print(mod,mod2)
print(list(set1))