class Subject(object):
    #represents what is being observed
    
    def __init__(self):
        self._observers = [] #this where references to all the observers
        
    def attach(self, observer):
        #if the observer is not already in the observers list
        #append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass 
        
    def notify(self, modifier=None):
        #for all the observers in the list
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Core(Subject):
    def __init__(self,name=""):
        super().__init__()
        self._name = name #name of core
        self._temp = 0 #the temperature of core
        
    @property #getter that gets the core temperature
    def temp(self):
        return self._temp
        
    @temp.setter  # Setter for core temperature
    def temp(self, value):
        self._temp = value
        # Notify the observers whenever the temperature changes
        self.notify()
    
    @property
    def name(self):
        return self._name
    
class TempViewer:
    def update(self, subject):#alert method 
        print("Temperature viewer: {} has temperature {}".format(subject.name, subject.temp))
            
# Create cores
c1 = Core("Core1")
c2 = Core("Core2")

# Create temperature viewers
v1 = TempViewer()
v2 = TempViewer()

# Attach viewers to Core1
c1.attach(v1)
c1.attach(v2)

# Change temperature and see notifications
c1.temp = 80
c1.temp = 90