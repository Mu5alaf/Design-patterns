class Dog:
    
    """Dog class"""
    
    def __init__(self,name):
        self._name = name
        
    def speak(self):
        return "woof!"
    def color(self):
        return "black"

def get_pet(pet="dog"):
    
    """The Factory Method"""
    
    pets = dict(dog=Dog("Hope"))
    return pets[pet]
        
class Cat:
    
    """Cat class"""
    
    def __init__(self,name):
        self._name = name
        
    def speak(self):
        return "meow!!"
    def color(self):
        return "yellow"

def get_pet(pet="cat"):
        
    """The Factory Method"""
        
    pets = dict(dog=Dog("Hope"),cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak(),d.color())

c = get_pet("cat")
print(c.speak(),c.color())
