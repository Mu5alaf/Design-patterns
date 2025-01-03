class Handler:
    
    def __init__(self,successor):
        self._successor = successor
    
    def handle(self,request):
        handled = self._handle(request)
        
        if not handled:
            self._successor.handle(request)
    
    def _handle(self,request):
        raise NotImplementedError("must provide implementation in subclass")
    
class ConcreteHandler1(Handler):
    
    def _handle(self, request):
        if 0 < request <= 10:
            print("Request {} handled in handelr 1".format(request))
            return True

class DefaultHandler(Handler):
    
    def _handle(self, request):
        print("end of chain, no handler for {}".format(request))
        return True
    

class Client:
    def __init__(self):
        self.handelr = ConcreteHandler1(DefaultHandler(None))
        
    def delegate(self,requests):
        for request in requests:
            self.handelr.handle(request)


c = Client()

requests = [2,5,11]

c.delegate(requests)