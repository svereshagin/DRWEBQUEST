class Cat:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return self.__class__.__name__ + "hello"
    
c = Cat("Cat")
print(c)
print([c])