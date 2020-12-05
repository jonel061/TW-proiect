import os

import cursor as cursor
import mysql.connector
from flask import Flask, render_template, request, sessions, redirect

app = Flask(__name__)

#app.secret_key = os.urandom(24)
conn = mysql.connector.connect(host="localhost", user="root", password="BarbuJonel1226", database="www")
cursor = conn.cursor()


@app.route('/map')
def map():
  return render_template('./map.html')


@app.route('/login')
def login():
    return render_template('./login.html')


@app.route('/register')
def about():
    return render_template('./register.html')


@app.route('/home')
def home():
    #  if 'user_id' in sessions:
    return render_template('./home.html')


# else:
#     return redirect('/')

@app.route('/login_validation',methods=['POST', 'GET'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute(""""SELECT * FROM `users` WHERE `email` LIKE '{}' AND  `password` LIKE '{}' """
                   .format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        sessions['user_id'] = 'users[0][0]'
        return render_template('home.html')
    else:
         return render_template('./login.html')



@app.route('/add_user', methods=['POST', 'GET'] )
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    pasword = request.form.get('upassword')

    cursor.execute(""""INSERT INTO `users` (`user_id`,`name`,`email`,`password`)VALUES
    (NULL,'{}','{}',{})""".format(name, email, pasword))
    conn.commit()

    cursor.execute(""""SELECT * FROM `users` WHERE `email` LIKE '{}' """.format(email))
    myuser = cursor.fetchall()
    sessions ['user_id']=myuser[0][0]
    return redirect('/home')

@app.route('/logout')
def logout():
  sessions.pop('user_id')
  return redirect('./login.html')




if __name__ == '__main__':
    app.run(debug=True)
