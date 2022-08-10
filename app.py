from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula python para Web"


@app.route("/usuario")
def usuario():
    usuario = [1, "Bibi","Aluna"]
    alunos = ["Bibi", "Bubu", "Bobo", "Baba"]
    return render_template('index.html', usuario=usuario, alunos=alunos)


@app.route("/contatos")
def contato():
    return render_template('index.html', usuario= usuario, nome=nomeAula)
