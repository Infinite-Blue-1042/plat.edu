from flask import *
from datetime import timedelta

app = Flask(__name__, template_folder='templates')
app.secret_key = 'NmhfpP8v'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/users/<user>')
def users(user):
    return render_template('users.html', user=user)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        session['user'] = request.form['nm']
        return redirect(url_for('users', user=session['user']))
    else:
        if 'user' in session:
            return redirect(url_for('users', user=session['user']))
        return render_template('login.html')


@app.errorhandler(403)
def not_found(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(port=8000)
