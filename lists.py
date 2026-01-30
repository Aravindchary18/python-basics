sub=["tel","hin","eng","mat",]
print(sub)
print(sub[-1])
sub.append("aag")
print(sub)
sub+=(["bull","973"])      
sub.remove("tel")
print(sub.pop())
sub.insert(1,"into")
sub[3:3]=["lulu","koko"]
print(sub)
print(sorted(sub,key=str.lower))
#lists are done ny brackets[], parenthesis are noy used for strings , you are using them to pass arguments to the function.ex=sub.replace()
#the fuction replace()or remove() like this we use them , inside we keep strings or according to your condition