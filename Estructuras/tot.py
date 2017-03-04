import graphviz as gvl
import os


class NodoLista(object):
	def __init__(self,elemento):
		self.elemento=elemento
		#self.palabra=palabra
		self.psig=None
	def getElemento(self):
		return self.elemento
	


class Lista(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
		self.tam=0
	def getVacio(self):
		if self.primero==None:
			return True

	def setInicio(self,elemento):
		nuevo = NodoLista(elemento)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			nuevo.psig=self.primero
			self.primero=nuevo
			self.tam +=1

	def setFinal(self,elemento):
		nuevo=NodoLista(elemento)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			self.ultimo.psig=nuevo
			self.ultimo=nuevo
			self.tam +=1
	
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
				#print(temp.getPalabra())
				if temp==self.ultimo:
					validar=False
				else:
					temp=temp.psig
	def buscar(self,elemento):
		if self.getVacio()==True:
			print("lista vacia")
		else:
			temp=self.primero
			while temp.getElemento()!=elemento:
				temp=temp.psig
			return temp.getElemento()
			print "se encontro el elemento ->"+temp.getElemento()

	
	def obtenerSize(self):
		return self.tam

	def eliminar(self,index):
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

	def graficar(self):
		auxiliar=self.primero
		auxiliar2=self.primero.psig
		file_path="Reporte"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
				print("se hizo el path")
			archivo=open("Reporte/lista.dot","w")
			archivo.write("digraph Lista{\n")
			archivo.write("\t node[shape=record];\n")
			archivo.write("\t subgraph clusterList {\n")
			archivo.write("\t label= \"lista\";\n")
			archivo.write("\t fontsize = 16;\n")
			while auxiliar!=None and auxiliar2!=None:
				archivo.write("\t" + str(auxiliar.getElemento())+"->"+str(auxiliar2.getElemento())+"\n")
				auxiliar=auxiliar.psig
				auxiliar2=auxiliar2.psig
			archivo.write("\t } \n")
			archivo.write("}")
			archivo.close()
			cmd='"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Reporte\\lista.dot -o Reporte\\lista.jpg'
			os.system(cmd)
		except ValueError:
			print("Error")
	
           
        
b=Lista()
b.setInicio("hola3")
b.setInicio("hola1")
b.setInicio("hola2")
b.graficar()

 




    


#para cola eliminar primero
#para pila el ultimo
