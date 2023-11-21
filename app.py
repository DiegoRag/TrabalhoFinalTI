
from flask import Flask, render_template, request, url_for, flash, redirect, session,send_from_directory



app = Flask(__name__)

app.config['SECRET_KEY'] = '07ced41fe132b166347a6f014a704f51aacfddf919ad41b182562d0668b344f8'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ciencia_humana')
def ciencia_humana():
    return render_template('ciencia_humana.html')

@app.route('/ciencia_natureza')
def ciencia_natureza():
    return render_template('ciencia_natureza.html')

@app.route('/linguagens')
def linguagens():
    return render_template('linguagens.html')

@app.route('/matematica')
def matematica():
    return render_template('matematica.html')

@app.route('/ti')
def ti():
    return render_template('ti.html')

@app.route('/Automacao')
def Automacao():
    return render_template('automacao.html')

@app.route('/Metaverso')
def Metaverso():
    return render_template('metaverso.html')

@app.route('/Realidade_aumentada')
def Realidade_aumentada():
    return render_template('realidade_aumentada.html')

@app.route('/Inteligencia_artificial')
def Inteligencia_artificial():
    return render_template('inteligencia_artificial.html')

@app.route('/Machine_learning')
def Machine_learning():
    return render_template('machine_learning.html')

@app.route('/Home_TI')
def Home_TI():
    return render_template('home_ti.html')

@app.route('/Home_escola')
def Home_escola():
    return render_template('home_escola.html')



if __name__ == '__main__':
    app.run(debug=True)
    