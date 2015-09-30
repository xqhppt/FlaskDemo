# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, request, session, flash, url_for, render_template,redirect,abort




app = Flask(__name__)
#app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_pyfile("Config/__init__.py")

userList = []
userList.append({"Name":"Lily1","Age":"20","Remark":"一个美女"})
userList.append({"Name":"Lily2","Age":"20","Remark":"一个美女"})
userList.append({"Name":"Lily3","Age":"20","Remark":"一个美女"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')

            return redirect(url_for('list'))

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('list'))

@app.route('/add', methods=['POST'])
def add():
    if not session.get('logged_in'):
        abort(401)

    name = request.form["Name"]
    age = request.form["Age"]

    global userList
    userList.append({"Name":name,"Age":age,"Remark":"一个美女"})

    flash('New entry was successfully posted')
    return redirect(url_for('list'))

@app.route('/')
def list():
    global userList

    return render_template('list.html', list=userList)


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])


