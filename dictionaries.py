sub={"name":"sad","age":"99","gen":"inf"}
print(sub["name"])
print(sub.get("gen"))
print(sub.pop("age"))
print(sub.items())
print(list(sub.items()))
print(len(sub))
del sub['name']
subcopy=sub.copy()
print(sub)
print(subcopy)