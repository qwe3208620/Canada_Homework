
import csv
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm

app = Flask(__name__)
app.secret_key='hehe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/index')
def index():
    return render_template("Base.html")


@app.route('/contact')
def contact_form():
    return render_template('contact_form.html')


@app.route('/contact_form', methods=['POST'])
def handle_contact_form2():
    with open('data/messages.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([request.form['name'], request.form['email'], request.form['message']])
    return render_template('contact_response.html', data=request.form)



@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username,password,password2]):
            flash ('参数不完整')
        elif password != password2:
            flash ('两次密码不一致，请重新输入')
        else:
            new_user = Users(username=username,password=password,id=None)
            db.session.add(new_user)
            db.session.commit()
            return ''
    return render_template('register.html')






@app.route("/login",methods=['POST','GET'])
def login():
    if request.method.lower() == 'get':
        return render_template("login.html")
    elif request.method.lower() == 'post':
        _reinfo=request.values
        _user='admin'
        _pass='123456'
        if request.form['username'] == _user and request.form['password'] == _pass:#验证成功
            session['username'] = _user
            return jsonify({'code': 200, 'msg': '登录成功'})
        else:
            return jsonify({'code': 400, 'msg': '用户名或密码错误'})





@app.route('/History')
def history():
    return render_template("History.html")


@app.route('/Food')
def food():
    return render_template("Food.html")


@app.route('/Cities')
def cities():
    return render_template("Cities.html")

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(10))
    password = db.Column(db.String(16))


if __name__ == '__main__':
    app.run()
