import time

class Producer:
    """Define  the 'resource-intensive' object to instantiate"""
    
    def produce(self):
        print("producer is working hard")
        
    def meet(self):
        print("producer has time to meet you now")

class Proxy:
    
    """define the relatively less resource intensive proxy to instantiate"""
    
    def __init__(self):
        self.occupied = 'no'
        self.producer = None
        
    def produce(self):
        """Check if producer is avaliable"""
        print("artist checking if producer is availibel...")
        
        if self.occupied == 'no':
            self.produce = Producer()
            time.sleep(2)
            self.produce.meet()
        else:    
            time.sleep(2)
            print("Producer is busy")

# instantiate a proxy 
p = Proxy()

#make proxy artist produce until producer is available
p.produce()

#change status
p.occupied = 'yes'

# make producer produce
p.produce()