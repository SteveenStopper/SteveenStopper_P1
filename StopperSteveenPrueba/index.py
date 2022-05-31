from flask import Flask, render_template #Imoprtamos la libreria Flask

app = Flask(__name__) #Inicializamos la variable.

@app.route('/') #Será responsable de mostrar la lista actual de tareas pendientes en una tabla HTML.
def index():    # y mostrar un formulario HTML para enviar un nuevo elemento de la lista de tareas pendientes.
   return render_template('main.html')

@app.route('/Usuario') #Será responsable de mostrar la lista actual de tareas pendientes en una tabla HTML.
def Usus():    # y mostrar un formulario HTML para enviar un nuevo elemento de la lista de tareas pendientes.
   return render_template('usuario.html')

if __name__ == '__main__': #Main del programa.
    app.run(debug=True)