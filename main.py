from ast import match_case
from flask import Flask, render_template, request


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
@app.route('/operasBas', methods=["GET", "POST"])
def operasBas():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    operacion = request.form.get("operacion")

    match(operacion):
        case "suma":
            res = float(n1) + float(n2)
        case "resta":   
            res = float(n1) - float(n2)
        case "multiplicacion":
            res = float(n1) * float(n2) 
        case "division":
            if float(n2) != 0:
                res = float(n1) / float(n2)
            else:
                res = "Error: División por cero no permitida."
        case _:
            res = ""

    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route('/resultado', methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    operacion = request.form.get("operacion")

    match(operacion):
        case "suma":
            return f"La suma de {n1} y {n2} es: {float(n1) + float(n2)}"
        case "resta":
            return f"La resta de {n1} y {n2} es: {float(n1) - float(n2)}"
        case "multiplicacion":
            return f"La multiplicación de {n1} y {n2} es: {float(n1) * float(n2)}"
        case "division":
            if float(n2) != 0:
                return f"La división de {n1} y {n2} es: {float(n1) / float(n2)}"
            else:
                return "Error: División por cero no permitida."
        case _:
            return "Operación no válida."


    return f"La suma de {n1} y {n2} es: {float(n1) + float(n2)}"

if __name__ == "__main__":
    app.run(debug=True)
