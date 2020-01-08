
"""
class AbstractAdapter:
	filas:int
	cols:int

	def getElement(self,x,y):
		pass


class Adapter(AbstractAdapter):
	def __init__(self,vec):
		self.vector=vec		

"""

class Abstract_Adapter():

	def get_element(self,i,j):
		pass



class Adaptee:  # VECTOR
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """
    def __init__(self,arreglo):
    	self.arreglo = arreglo

    def get(self,i,j):
        return self.arreglo[j-1+(i-1)*4]


class Adapter(Abstract_Adapter):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee,fil,col):
    	self.filas= fil
    	self.col=col
        self.adaptee = adaptee

    def request(self,i,j):
        return self.adaptee.get(i,j)




x = [1,2,3,4,5,6,7,8,9,10,11,12]

adaptee = Adaptee(x)

adapter = Adapter(adaptee,3,4)

print(adapter.request(2,2))