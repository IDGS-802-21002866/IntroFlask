from flask import Flask, render_template
from flask.cli import F


app = Flask(__name__)


@app.route("/")
def index():
    titulo = "IDGS-802-FLASK"
    lista = ["Juan", "María", "Pedro", "Ana"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/reportes")
def reportes():
    return render_template("reportes.html")


@app.route("/formularios")
def formularios():
    return render_template("formularios.html")


@app.route("/hola")
def hola():
    return "¡Hola, hola!"


@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"


@app.route("/numero/<int:n>")
def numero(n):
    return f"El número es: {n}"


@app.route("/user/<int:id>/<string:username>")
def user_info(id, username):
    return f"ID: {id}, Username: {username}"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma de {n1} y {n2} es: {n1 + n2}"


@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1>Hola, {param}!</h1>"


@app.route("/operas")
def operas():
    return """
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="apellidoPaterno">Apellido paterno:</label>
            <input type="text" id="apellidoPaterno" name="apellidoPaterno" required>
        </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
