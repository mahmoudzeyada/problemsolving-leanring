from decoratores import test,timer

@test
def x(name):
    print("heloo"+name)


x("mahmoud")

@test
def greet():
    print ("heloo")
    return "hi"
print (greet())

def y():
    print ("test")
    return "test1"

x=y()

@timer
def waste_some_time(num_times):
    for _ in range(1000):
        print (sum([_*2 for _ in range(1000*10**10)]))
waste_some_time(1000000000000000000000000000000000000000000000000000*100000000000)