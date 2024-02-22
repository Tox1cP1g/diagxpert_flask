from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
   if request.method == 'POST':
       Login = request.form.get('Login')
       Password = request.form.get('Password')

       db_lp = sqlite3.connect('login_password.db')
       cursor_db = db_lp.cursor()
       cursor_db.execute(('''SELECT password FROM passwords
                                               WHERE login = '{}';
                                               ''').format(Login))
       pas = cursor_db.fetchall()

       cursor_db.close()
       try:
           if pas[0][0] != Password:
               return render_template('auth_bad.html')
       except:
           return render_template('auth_bad.html')

       db_lp.close()
       return render_template('successfulauth.html')

   return render_template('authorization.html')

@app.route('/registration', methods=['GET', 'POST'])
def form_registration():

   if request.method == 'POST':
       Login = request.form.get('Login')
       Password = request.form.get('Password')

       db_lp = sqlite3.connect('login_password.db')
       cursor_db = db_lp.cursor()
       sql_insert = '''INSERT INTO passwords VALUES('{}','{}');'''.format(Login, Password)


       cursor_db.execute(sql_insert)

       cursor_db.close()

       db_lp.commit()
       db_lp.close()

       return render_template('successfulregis.html')

   return render_template('registration.html')


if __name__ == "__main__":
 # app.run(debug=True)
    app.run()