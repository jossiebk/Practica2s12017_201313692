import cola
import tot
import pila
x=cola.Cola()

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

@app.route("/e")
def hellof():
	return "Hello World2!"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
