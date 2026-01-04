
#def c(x,y):
    
    #num10 = 10
   # print(num10)
  #  z = x*y
 #   return z

#print(c(3,4))


#global num10
#num10 = 20
#def add(x,y=0,z=1):
    #print(num10)
   # result = x + y + z
 ##   return result
#num10 = 10
#num20 = 20
#sab = print(add(num20))

#def my(*args,**kwargs):
    #for arg in args:
   #     print(arg)
  #  for kwarg in kwargs.items():
 #       print(kwarg)
        
        
#adda = my("hari","shari",last="hos",boss="gosh")
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hasto(self):
        print(f"this is{self.name} and i love myself ")
            
koho = person("arbind",24)
joho = person("salam",22)

koho.hasto()

class car:
    var = 4
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def gaadi(self):
        print(f"this is my car {self.name} amd i love {self.model}")
    
car1 = car("toyota","abascus")
car2 = car("lexus","pricey")

car1.gaadi()

class Dog:
    def __init__(self,name):
        self.name = name
        print(name)

    def meow(self):
        return "meow"

    def bark(self):
        print(f"bark and {self.name}")

d = Dog("tim")

print(type(d))

class animal:
    def hen(self):
        return"hen is mother"

class human:
    def manxe(self):
        return "sarbashertsa"
class chick(animal,human):
    def sano(self):
        return "im chick"

chick2 = chick()
print(chick2.sano())

print(chick2.hen())#this one is parenting
print(chick2.manxe())


class a:
    def method_a(self):
        return"grandf"
class b(a):
    def method_b(self):
        return"parents"
class c(b) :
    def method_c(self):
        return "the child"
    
obj_c = c()
print(obj_c.method_a())
print(obj_c.method_b())#multilevel inheritance


class rect():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
            return self.length*self.breadth
class square(rect):
    def __init__(self,sides):
        super().__init__(sides,sides)#yesley chai parenting ko conducor lai use garxa
    
sq=square(4)
print(sq.area())


    





        



