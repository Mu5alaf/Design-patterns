class Dog:
    
    """one of the objects to be returuned"""
    
    def speak(self):
        return "woof!"
    
    def color(self):
        return "black"
    
    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""
    
    def get_pet(self):
        """returns a dog objects"""
        return Dog()
    def get_food(self):
        """returns a dog food objects"""
        return "Dog food"

class petStore:
    """petStore houses our abstract factory"""
    
    def __init__(self,pet_factory=None):
        """pet_factory our abstract factory"""
        self._pet_factory = pet_factory
        
    def show_pet(self):
        """utility method to display the details of objects returen """
        
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print("our pets is '{}'".format(pet))
        print("our pets say hello by '{}'".format(pet.speak()))
        print("its food is '{}'".format(pet_food))

#create a concrete factory
factory = DogFactory()

#create a pet store housing our abstract factory
shop = petStore(factory)

#invoke the utility method to  show the details of our pet
shop.show_pet()
