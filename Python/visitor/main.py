class House(object):
    def accept(self,visitor):
        visitor.visit(self)
        
    def work_on_hvac(self, hvac_specialist):
        print(self, "work on by", hvac_specialist)
        
    def work_on_electricity(self,electricain):
        print(self, "work on by", electricain)

    def __str__(self):
        return self.__class__.__name__

class Visitor(object):
    def __str__(self):
        return self.__class__.__name__
    
class HvacSpecialist(Visitor):
    
    def visit(self,house):
        house.work_on_hvac(self)
        

class Electrican(Visitor):
    
    def visit(self, house):
        house.work_on_electricity(self)



hv = HvacSpecialist()

e = Electrican()

home = House()

home.accept(hv)

home.accept(e)