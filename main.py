from flask import Flask, render_template, request, flash, redirect, url_for
import os

#cria a aplicação flask
app = Flask(__name__)
app.secret_key = 'chave-secreta'
#definir uma rota
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    message = request.form['message']
    text =  f"Email: {email} your message: {message}"
    with open('contact.txt','a', newline='') as file:
        if message != '':
            file.write(text + os.linesep)
    return redirect(url_for('home'))
#inicia a aplicação pelo arquivo main
if __name__ == "__main__":
    app.run(debug=True)