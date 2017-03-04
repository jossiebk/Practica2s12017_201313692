import graphviz as gvs
import os
#nodo de mi pila
class NodoPila(object):
	def __init__(self,elemento):
		self.elemento=elemento
		self.psig=None
	def getElemento(self):
		return self.elemento
	
#clase pila
class Pila(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
	def getVacio(self):
		if self.primero==None:
			return True

	def setInicio(self,elemento):
		nuevo = NodoPila(elemento)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			nuevo.psig=self.primero
			self.primero=nuevo

	def setFinal(self,elemento):
		nuevo=NodoPila(elemento)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			self.ultimo.psig=nuevo
			self.ultimo=nuevo
	def eliminarPrimero(self):
		if self.getVacio()==True:
			print ("lista vacia, imposible eliminar")
		elif self.primero==self.ultimo:
			self.primero=None
			self.ultimo=None
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
				
				if temp==self.ultimo:
					validar=False
				else:
					temp=temp.psig
	def graficar(self):
		auxiliar=self.primero
		auxiliar2=self.primero.psig
		file_path="Reporte"
		try:
			if not os.path.exists(file_path):
				os.makedirs(file_path)
				print("se hizo el path")
			archivo=open("Reporte/pila.dot","w")
			archivo.write("digraph Pila{\n")
			archivo.write("\t node[shape=record];\n")
			archivo.write("\t subgraph clusterPila {\n")
			archivo.write("\t label= \"pila\";\n")
			archivo.write("\t fontsize = 16;\n")
			while auxiliar!=None and auxiliar2!=None:
				archivo.write("\t" + str(auxiliar.getElemento())+"->"+str(auxiliar2.getElemento())+"\n")
				auxiliar=auxiliar.psig
				auxiliar2=auxiliar2.psig
			archivo.write("\t } \n")
			archivo.write("}")
			archivo.close()
			cmd='"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Reporte\\pila.dot -o Reporte\\pila.jpg'
			os.system(cmd)
		except ValueError:
			print("Error")


