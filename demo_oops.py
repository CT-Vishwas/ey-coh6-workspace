class Person:
    # __slots__ = ["name","city"]
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def __repr__(self):
        return f"Person Name: {self.name}, City: {self.city}"

# class User(Person):
#     def __init__(self, name, city, age):
#         super().__init__(name, city)
#         self.age = age

#     def __repr__(self):
#         return f"Person Name: {self.name}, City: {self.city}, Age:{self.age}"

p1 = Person("vishwas","Pune")
print(p1)
p2 = Person("Raj", "Delhi")
print(p2)

# p3 = User("Riya","Delhi",20)
# print(p3)

#p2.salary = 200000
# print(p2.salary)
# print(p2.__dict__)