#return means it simply return the value to the caller , means the value you keep after return it equals to the value inside the caller,read  next # for understanding.
#return wrapper , wrapper function returns to the caller and equals to the func because this func is placed in it.
#when we use decorator symbolf af any function above, that fuction becomes original function and this function is equal to the decorator caller function which we name as func in this , so it euals to func , since func is updated to wrapper now this sayhi is equal to wrapper.
#return result makes the wrapper give back the original function value when you type sayhi
def anyvariable(func):
    def wrapper():
        print("before")
        result=func()
        print("after")
        return result
    return wrapper

@anyvariable
def sayhi():
    print("yoyo")

sayhi()



