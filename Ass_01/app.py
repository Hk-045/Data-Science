<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9991787762hk'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

@app.route('/')
def registration_form():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        Student_name = request.form['Student_name']
        Father_name = request.form['Father_name']
        Mother_name = request.form['Mother_name']
        Phone_number = request.form['Phone_number']
        Email = request.form['Email']
        Date_of_birth = request.form['Date_of_birth']
        Address = request.form['Address']
        Blood_group = request.form['Blood_group']
        Department = request.form['Department']
        Course = request.form['Course']
        Password = request.form['Password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (Student_name, Father_name, Mother_name, Phone_number, Email, Date_of_birth ,Address, Blood_group, Department, Course, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (Student_name, Father_name, Mother_name, Phone_number, Email, Date_of_birth, Address, Blood_group,  Department, Course, Password))
        mysql.connection.commit()
        cur.close()

        return render_template('submit.html')

if __name__ == '__main__':
=======
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9991787762hk'
app.config['MYSQL_DB'] = 'registration_db'

mysql = MySQL(app)

@app.route('/')
def registration_form():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        Student_name = request.form['Student_name']
        Father_name = request.form['Father_name']
        Mother_name = request.form['Mother_name']
        Phone_number = request.form['Phone_number']
        Email = request.form['Email']
        Date_of_birth = request.form['Date_of_birth']
        Address = request.form['Address']
        Blood_group = request.form['Blood_group']
        Department = request.form['Department']
        Course = request.form['Course']
        Password = request.form['Password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (Student_name, Father_name, Mother_name, Phone_number, Email, Date_of_birth ,Address, Blood_group, Department, Course, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (Student_name, Father_name, Mother_name, Phone_number, Email, Date_of_birth, Address, Blood_group,  Department, Course, Password))
        mysql.connection.commit()
        cur.close()

        return render_template('submit.html')

if __name__ == '__main__':
>>>>>>> bbbeab9 (First Commit)
    app.run(debug=True)