from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Ejercicio1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3  = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        #promedio
        promedio =(nota1 + nota2 + nota3) / 3
        estado ="Aprobado" if promedio >=40 and asistencia >=75 else "Reprobado"
        return render_template('resultado1.html', promedio=promedio, estado=estado)
    return render_template('formulario.html')

#Ejercicio2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        #nombre con mas caracteres
        nombre_mas_largo = max([nombre1, nombre2, nombre3], key=len)
        longitud = len(nombre_mas_largo)

        return render_template('resultado2.html', nombre=nombre_mas_largo, longitud=longitud)
    return render_template('formulario2.html')

if __name__ == '__main__':
    app.run()