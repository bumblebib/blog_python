from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
    return """
    <html>
        <head>
            <title> Contatos </title>
        </head>

        <body>
            <h1>Bibi, e-mail</h1>
            <h2>bibibubu@hotmail.com</h2>
            <h3>15 555 5555 555</h3>
        </body>
    </html>
    """