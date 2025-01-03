from functools import wraps

def make_blink(function):
    """defines the decorator"""
    
    #this makes the decorator transparent in terms of its name and docs
    @wraps(function)
    
    #define the inner function
    def decorator():
        #grab the retuern value if the function being decorated
        ret = function()
        #add_new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"
    return decorator

#apply the decorator here

@make_blink
def hello_world():
    
    """Orginal Function"""

    return "Hello, World!"

#with decorator
print(hello_world())

# orginal function
print(hello_world.__name__)
print(hello_world.__doc__)
