from flask import  Flask





app = Flask(__name__)
try:
    from kibo.Employee.route import employees
except :
    print("error start from here")
app.register_blueprint(employees)