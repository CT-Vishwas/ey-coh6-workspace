m = 100
def func():
    pass

def display(message):
    global m
    m = 75
    print(f"m inside display: {m}")
    print(f"Message: {message}")

# def add(a,b,c, z= 0,x=25):
#     print(f"m inside add: {m}")
#     return a+b+z

def add(*args):
    return sum(args)

def display_dict(**kwargs):
    for k,v in kwargs.items():
        print("|",k,"|",v)

# print(f"m global before call: {m}")
# display("Hello Vishwas")
# print(add(23,45, 67))
# print(add(23,45, 67,100,34,45,97,89))
# print(f"m global after call: {m}")
d1 = {}

display_dict(user="vishwas",city="Pune")
display_dict(user="arjun",city="Delhi",age=25)

# Pointer kind of advanced approach
# d2 = {"user":"Raj","city":"Delhi","age":25}
# display_dict(**d2)