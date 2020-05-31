from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/vue1.html')
def vue1():
    return render_template('vue1.html')

@app.route('/vue2.html')
def vue2():

    return render_template('vue2.html')

@app.route('/Statsvue1.html')
def Statsvue1():
    return render_template('Statsvue1.html')

@app.route('/Statsvue2.html')
def Statsvue2():
    return render_template('Statsvue2.html')

@app.route('/Accueil.html')
def Accueil():
    return render_template('Accueil.html')

@app.route('/vue2.html', methods=('GET', 'POST'))
def liste():
    if request.method == 'POST':
        idChamp = request.form['championnat']
        print(idChamp)
