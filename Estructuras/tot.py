class NodoLista(object):
	def __init__(self,elemento,palabra):
		self.elemento=elemento
		self.palabra=palabra
		self.psig=None
	def getElemento(self):
		return self.elemento
	def getPalabra(self):
		return self.palabra









class Lista(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.tam=0
	def getVacio(self):
		if self.primero==None:
			return True

	def setInicio(self,elemento,palabra):
		nuevo = NodoLista(elemento,palabra)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			nuevo.psig=self.primero
			self.primero=nuevo
			self.tam +=1

	def setFinal(self,elemento,palabra):
		nuevo=NodoLista(elemento,palabra)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			self.ultimo.psig=nuevo
			self.ultimo=nuevo
			self.tam +=1
	def eliminarPrimero(self):
		if self.getVacio()==True:
			print ("lista vacia, imposible eliminar")
		elif self.primero==self.ultimo:
			self.primero=None
			self.ultimom=None
			print("elemento eliminado, lista vacia")
		else: 
			temp =self.primero
			self.primero=self.primero.psig
			temp=None
			print("elemento eliminado")
	def eliminarUltimo(self):
		if self.getVacio()==True:
			print("lista vacia")
		elif self.primero==self.ultimo:
			self.primero=None
			self.ultimo=None
			print("elemento eliminado, lista vacia")
		else:
			validar=True
			temp=self.primero
			while(validar):
				if temp.psig==self.ultimo:
					temp2=self.ultimo
					self.ultimo=temp
					temp2=None
					validar=False
					print("elemento eliminado")
				else:
					temp=temp.psig
	def getPrimero(self):
		if self.getVacio()==true:
			return ("lista vacia")
		else:
			return self.primero
	def getUltimo(self):
		if self.getVacio()==true:
			return ("lista vacia")
		else:
			return self.ultimo
	def imprimirInicioFin(self):
		if self.getVacio()==True:
			print("lista vacia")
		else:
			validar=True
			temp=self.primero
			while(validar):
				print(temp.getElemento())
				print(temp.getPalabra())
				if temp==self.ultimo:
					validar=False
				else:
					temp=temp.psig
	def buscar(self,palabra):
		if self.getVacio()==True:
			print("lista vacia")
		else:
			temp=self.primero
			while temp.getPalabra()!=palabra:
				temp=temp.psig
			print "se encontro el elemento ->" + temp.getPalabra()

	
	def obtenerSize(self):
		return self.tam

	def eliminar2(self,index):
		if index>=0 and index<self.tam:
			if index==0:
				self.primero=self.primero.psig
			elif index==self.obtenerSize()-1:
				actual=self.primero
				while actual.psig!=self.ultimo:
					actual=actual.psig
				aux=actual.psig
				actual.psig=None
				self.ultimo=actual
			else:
				aux=self.primero
				contador=0
				while contador<index-1:
					aux=aux.psig
					contador+=1
				siguiente=aux.psig
				aux.psig=siguiente.psig
				aux=None
		self.tam-=1

				




	

   
    			

                        
	

x=Lista()
x.setFinal(2,"hola")
x.setFinal(3,"python")
x.setFinal(7,"qer")
x.setFinal(1,"queso")
x.setFinal(90,"pan")
x.setFinal(17,"adios")
x.setFinal(11,"nike")
x.setFinal(45,"ter")



x.imprimirInicioFin()
print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
#x.buscar("queso")
x.eliminar2(4)
x.imprimirInicioFin()  

 




    


#para cola eliminar primero
#para pila el ultimo
