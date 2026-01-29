import math
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.secret_key = "Clave secreta"
csrf = CSRFProtect()


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


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/usuarios", methods=["POST", "GET"])
def usuarios():
    matricula = 0
    nombre = ""
    apellidoPaterno = ""
    apellidoMaterno = ""
    correo = ""

    usuarios_class = forms.UserForm(request.form)

    if request.method == "POST" and usuarios_class.validate():
        matricula = usuarios_class.matricula.data
        nombre = usuarios_class.nombre.data
        apellidoPaterno = usuarios_class.apellidoPaterno.data
        apellidoMaterno = usuarios_class.apellidoMaterno.data
        correo = usuarios_class.correo.data

        mensaje = f"Bienvenido {nombre}"
        flash(mensaje)

    return render_template(
        "usuarios.html",
        form=usuarios_class,
        matricula=matricula,
        nombre=nombre,
        apellidoPaterno=apellidoPaterno,
        apellidoMaterno=apellidoMaterno,
        correo=correo,
    )


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


@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    operacion = request.form.get("operacion")

    match (operacion):
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


@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = None

    if request.method == "POST":
        x1 = request.form.get("x1")
        x2 = request.form.get("x2")
        y1 = request.form.get("y1")
        y2 = request.form.get("y2")

        resultado = math.sqrt(
            math.pow(float(x2) - float(x1), 2) + math.pow(float(y2) - float(y1), 2)
        )
        return render_template("distancia.html", resultado=resultado)

    return render_template("distancia.html", resultado=resultado)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)
