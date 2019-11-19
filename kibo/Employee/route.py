from flask import Blueprint,jsonify,render_template,request,flash,session
from kibo.Employee.employee import Employee

from kibo.Employee.form import LoginForm



employees = Blueprint('employees', __name__,url_prefix="/employee")
hello = Employee()

@employees.route("/login/",methods=["GET","POST"])
def login():

    msg = ''
    form = LoginForm()
    username = form.username.data
    password = form.password.data
    if form.validate_on_submit():
        if request.method == "POST":
            row = hello.login(username,password)
            if type(row) == str:
                msg = row
            else:
                session["person_id"] = row["person_id"]
                session["loging_in"] = True
                return jsonify(row)

    return render_template("login.html",msg=msg,form=form)


@employees.route("/save/",methods=["GET","POST"])
def save():
    if session :
        return str(session["person_id"])
    else:
        return jsonify("error ")

