#nodo de mi pila
class NodoCola(object):
	def __init__(self,elemento):
		self.__elemento=elemento
		self.__psig=None
	def getElemento(self):
		return self.__elemento
	
#clase pila
class Cola(object):
	def __init__(self):
		self.__primero=None
		self.__ultimo=None
	def getVacio(self):
		if self.__primero==None:
			return True

	

	def queue(self,elemento):
		nuevo=NodoCola(elemento)
		if self.getVacio()==True:
			self.__primero=self.__ultimo=nuevo
		else:
			self.__ultimo.psig=nuevo
			self.__ultimo=nuevo
	def dequeue(self):
		if self.getVacio()==True:
			print ("lista vacia, imposible eliminar")
		elif self.__primero==self.__ultimo:
			self.__primero=None
			self.__ultimom=None
			print("elemento eliminado, lista vacia")
		else: 
			temp =self.__primero
			self.__primero=self.__primero.psig
			temp=None
			print("elemento eliminado")
	
	def getPrimero(self):
		if self.getVacio()==true:
			return ("lista vacia")
		else:
			return self.__primero
	def getUltimo(self):
		if self.getVacio()==true:
			return ("lista vacia")
		else:
			return self.__ultimo
	def mostrar(self):
		if self.getVacio()==True:
			print("lista vacia")
		else:
			validar=True
			temp=self.__primero
			while(validar):
				print(temp.getElemento())
				
				if temp==self.__ultimo:
					validar=False
				else:
					temp=temp.psig


x=Cola()
x.queue(2)
x.queue(12)
x.queue(90)
x.queue(23)
x.queue(77)

x.mostrar()

x.dequeue()
x.mostrar()