from kibo import app
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
import secrets

mysql = MySQL()

bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config["MYSQL_DATABASE_HOST"] = "127.0.0.1"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "kata"


mysql.init_app(app)
