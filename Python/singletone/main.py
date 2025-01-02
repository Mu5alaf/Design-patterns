class Borg:
    """
    the Borg design pattern
    """
    _shared_data = {} # attribute dictionary
    
    def __init__(self):
        self.__dict__ = self._shared_data # make an  attribute dictionary
        
class Singleton(Borg):
    """the singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) #update the attribute dictionary by inserting a new key value pair
        
    def __str__(self):
        return str(self._shared_data) # returns the attribute dictionary for printing
        
x  = Singleton()
s1 = Singleton(HTTP = "Hyper Test Transfer Protocol")
s2 = Singleton(HTTPS = "Hyper Test Transfer Protocol Secure")

print(x)