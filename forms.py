from wtforms import Form, StringField, IntegerField, PasswordField, EmailField, validators  # type: ignore


class UserForm(Form):
    matricula = IntegerField(
        "Matricula",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(
                min=100, max=1000, message="Ingrese un valor valido"
            ),
        ],
    )
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=1, max=20, message="Ingrese un nombre valido"),
        ],
    )
    apellidoPaterno = StringField(
        "Apellido paterno", [validators.DataRequired(message="El campo es requerido")]
    )
    apellidoMaterno = StringField(
        "Apellido materno", [validators.DataRequired(message="El campo es requerido")]
    )
    correo = EmailField(
        "Correo", [validators.DataRequired(message="El campo es requerido")]
    )
