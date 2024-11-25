from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/ejercicio1',methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado=''
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        pintura = int(request.form['pintura'])

        totalSinDesc = 9000*pintura

        if edad >= 18 and edad <= 30:

            desc = totalSinDesc * (15/100)
            valor_con_descuento = totalSinDesc - desc
            return render_template('ejercicio1.html', nombre=nombre, totalSinDesc=totalSinDesc, descuento=desc,
                                   totalApagar=valor_con_descuento, resultado='resultado')
        elif edad > 30:
            desc = totalSinDesc *(25/100)
            valor_con_descuento = totalSinDesc - desc
            return render_template('ejercicio1.html', nombre=nombre, totalSinDesc=totalSinDesc, descuento=desc,
                                   totalApagar=valor_con_descuento, resultado='resultado')
        else :
            return render_template('ejercicio1.html', nombre=nombre, totalSinDesc=totalSinDesc, descuento=0,
                                   totalApagar=totalSinDesc, resultado='resultado')

    return render_template('ejercicio1.html')


@app.route('/ejercicio2',methods=['GET', 'POST'])
def ejercicio2():
    if request.method =='POST':
        nombre = str(request.form['nombre'])
        contraseña = str(request.form['contraseña'])

        if nombre == 'juan' and contraseña == 'admin':
            return render_template('ejercicio2.html', nombre=nombre, rol= 'Administrador',resultado='resultado')
        elif nombre == 'pepe' and contraseña == 'user':
            return render_template('ejercicio2.html', nombre=nombre, rol='Usuario', resultado='resultado')
        else:
            return render_template('ejercicio2.html',error='error')

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)