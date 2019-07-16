class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return 'my name is {} and i am {} years old'.format(self.name, self.age)

class Cat(Pet):
    def __init__(self, name, age):
        super(Cat, self).__init__(name, age)

class Dog(Pet):
    def __init__(self, name, age):
        super(Dog, self).__init__(name, age)

dog01 = Dog('tom', 2)
cat01 = Cat('kitty', 3)
print(dog01.info())
print(cat01.info())
