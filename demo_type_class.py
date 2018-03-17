#使用type动态创建类

def sayHi(self):
    print("hi "+self.name)

a=type("Hello",(object,),{"name":"jack","sayHi":sayHi})

b=a()

print(b.name)
b.sayHi()

print(type(a))
print(type(b))