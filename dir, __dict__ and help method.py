#      dir() method >>>>>>>

x = [1,2,3]
print(dir(x))
print(x.__class_getitem__)

#        __dict__ attribute >>>>>>

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = person("umer nawaz", 22)
print(p.__dict__)

#   help() method >>>
print(help(person))