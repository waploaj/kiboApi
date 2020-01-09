from flask import  Flask
import  logging
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    mailhost='',
    fromaddr='',
    toaddrs=[''],
    subject=''
)
mail_handler.setLevel(logging.WARNING)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s)'))

app = Flask(__name__)
try:
    from kibo.Employee.route import employees
except :
    print("error start from here")
app.register_blueprint(employees)