class Korean:
    
    """Korean speaker"""
    
    def __init__(self):
        self.name = "Korean"
        
    def speak_korean(self):
        return "an-neyong?"
    

class British:
    
    """British speaker"""
    
    def __init__(self):
        self.name = "British"
        
    def speak_english(self):
        return "Hello!"


class Adapter:
    """ change the generic method name to indvidualized method"""
    def __init__(self, object, **adapter_method):
        
        """change the name of method"""
        
        self._object = object
        #add_a new dictionary item that establish the mapping a generic method name
        self.__dict__.update(adapter_method)
        
        
    def __getattr__(self, attr):
        """retuern attributes"""
        return getattr(self._object, attr)
    

objects = []

korean = Korean()
    
british = British()

objects.append(Adapter(korean, speak = korean.speak_korean))
objects.append(Adapter(british, speak = british.speak_english))

for obj in objects:
    print("{} says {} \n ".format(obj.name, obj.speak()))