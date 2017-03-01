class Nodo(object):
	def __init__(self,elemento,palabra):
		self.__elemento=elemento
		self.__palabra=palabra
		self.__psig=None
	def getElemento(self):
		return self.__elemento
	def getPalabra(self):
		return self.__palabra

class Lista(object):
	def __init__(self):
		self.__primero=None
		self.__ultimo=None
	def getVacio(self):
		if self.__primero==None:
			return True

	def setInicio(self,elemento,palabra):
		nuevo = Nodo(elemento,palabra)
		if self.getVacio()==True:
			self.__primero=self.__ultimo=nuevo
		else:
			nuevo.psig=self.__primero
			self.__primero=nuevo

	def setFinal(self,elemento):
		nuevo=Nodo(elemento)
		if self.getVacio()==True:
			self.__primero=self.__ultimo=nuevo
		else:
			self.__ultimo.psig=nuevo
			self.__ultimo=nuevo
	def eliminarPrimero(self):
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
	def eliminarUltimo(self):
		if self.getVacio()==True:
			print("lista vacia")
		elif self.__primero==self.__ultimo:
			self.__primero=None
			self.__ultimo=None
			print("elemento eliminado, lista vacia")
		else:
			validar=True
			temp=self.__primero
			while(validar):
				if temp.psig==self.__ultimo:
					temp2=self.__ultimo
					self.__ultimo=temp
					temp2=None
					validar=False
					print("elemento eliminado")
				else:
					temp=temp.psig
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
	def imprimirInicioFin(self):
		if self.getVacio()==True:
			print("lista vacia")
		else:
			validar=True
			temp=self.__primero
			while(validar):
				print(temp.getElemento())
				print(temp.getPalabra())
				if temp==self.__ultimo:
					validar=False
				else:
					temp=temp.psig
	

  
	


    
x=Lista()
x.setInicio(2,"hola")
x.setInicio(3,"python")
x.setInicio(7,"qer")
x.setInicio(1,"queso")
x.setInicio(90,"pan")



x.imprimirInicioFin()
x.eliminarUltimo()
x.imprimirInicioFin()

#para cola eliminar primero
#para pila el ultimo