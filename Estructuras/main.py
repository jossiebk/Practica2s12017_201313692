import cola
import tot
import pila
x=cola.Cola()
y=pila.Pila()
z=tot.Lista()

from flask import Flask, request, Response
app = Flask("EDD_jossie_server")

#Ejemplo de una clase, todos los metodos de las clases deben de tener como parametro el "self", que es como el .this en Java
class Usuario():
    def __init__(self, password, correo, nombre):
        self.nombre = nombre
        self.password = password
        self.correo = correo

@app.route('/metodoWeb',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = request.form['dato2']
	return "Hola que tal " + str(parametro) + "!"

@app.route('/AddCola',methods=['POST'])
def AgregarCola():
	T=str(request.form['valor'])
	x.queue(T)
	x.graficar()
	return "encolo "+str(T)
@app.route('/PopCola',methods=['POST'])
def EliminarCola():
	T=str(request.form['valor'])
	x.dequeue()
	x.graficar()
	return "elimino "
@app.route('/AddPila',methods=['POST'])
def AgregarPila():
	T=str(request.form['valor'])
	y.setInicio(T)
	y.graficar()
	return "metio en la pila ->"+str(T)
@app.route('/PopPila',methods=['POST'])
def EliminarPila():
	R=str(request.form['valor'])
	y.eliminarPrimero()
	y.graficar()
	return "salio ->"









@app.route('/AddLista',methods=['POST'])
def AgregarLista():
	T=str(request.form['valor'])
	Y=str(request)
	z.setInicio()
	z.graficar()
	return "elimino "
@app.route('/searchLista',methods=['POST'])
def BuscarLista():
	T=str(request.form['valor'])
	y.buscar(T)
	y.graficar()
	return "se encontro ->"+y.buscar(T)
@app.route('/popLista',methods=['POST'])
def EliminarLista():
	R=str(request.form['valor'])
	y.eliminar(R)
	z.graficar()
	return "salio ->"




@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
