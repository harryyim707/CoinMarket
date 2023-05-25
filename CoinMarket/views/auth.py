from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' "usr_id" in request.form and "usr_nm" in request.form and "usr_email" in request.form and "usr_pwd" in request.form and "repeat_pwd" in request.form:
        usr_id = request.form["usr_id"]
        usr_nm = request.form["usr_nm"]
        usr_email = request.form["usr_email"]
        usr_pwd = request.form["usr_pwd"]
        repeat_pwd = request.form["repeat_pwd"]

