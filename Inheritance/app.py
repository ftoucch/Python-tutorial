class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
    

class Cat(Mammal):
    def meow(self):
        print("annoing cat")

mycat = Cat()
mycat.meow