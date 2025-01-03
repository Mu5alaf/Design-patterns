class Component(object):
    """abstract class"""
    
    def __init__(self, *args, **kwargs):
        pass
    
    def component_function(self):
        pass
    

#inherits from the abstract class Compnent
class Child(Component):
    """concrete class"""
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
    
    def component_function(self):
        print("{}".format(self.name))

class Composite(Component):
    #inherites form abstract class Component
    
    def __init__(self, *args, **kwargs):
        Component.__init__(self,*args, **kwargs)
        #this where we store the name of composite obj
        self.name = args[0]
        #this where we keep our child items
        self.childern = []
    
    #add_method
    def append_child(self,child):
        """method to add  a new child item"""
        self.childern.append(child)
    
    #remove method
    def remove_child(self,child):
        self.childern.remove(child)
    
    def component_function(self):
        print("{}".format(self.name))
        
        for i in self.childern:
            i.component_function()


sub1 = Composite("submenu1")
sub11 = Child("submenu11")
sub12 = Child("submenu12")

sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("top_menu")

sub2 = Child("submune2")

top.append_child(sub1)

top.append_child(sub2)


top.component_function()