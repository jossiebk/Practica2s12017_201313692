import os
import graphviz
#nodo de mi pila
class NodoCola(object):
	def __init__(self,elemento):
		self.elemento=elemento
		self.psig=None
	def getElemento(self):
		return self.elemento
	
#clase pila
class Cola(object):
	def __init__(self):
		self.primero=None
		self.ultimo=None
	def getVacio(self):
		if self.primero==None:
			return True

	

	def queue(self,elemento):
		nuevo=NodoCola(elemento)
		if self.getVacio()==True:
			self.primero=self.ultimo=nuevo
		else:
			self.ultimo.psig=nuevo
			self.ultimo=nuevo
	def dequeue(self):
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
	def mostrar(self):
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
			archivo=open("Reporte/cola.dot","w")
			archivo.write("digraph Cola{\n")
			archivo.write("\t node[shape=ellipse, color=green,style=filled];\n")
			archivo.write("\t subgraph clusterCola {\n")
			archivo.write("\t label= \"cola\";\n")
			archivo.write("\t fontsize = 16;\n")
			while auxiliar!=None and auxiliar2!=None:
				archivo.write("\t" + str(auxiliar.getElemento())+"->"+str(auxiliar2.getElemento())+"\n")
				auxiliar=auxiliar.psig
				auxiliar2=auxiliar2.psig
			archivo.write("\t } \n")
			archivo.write("}")
			archivo.close()
			cmd='"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe" -Tjpg Reporte\\cola.dot -o Reporte\\cola.jpg'
			os.system(cmd)
		except ValueError:
			print("Error")


