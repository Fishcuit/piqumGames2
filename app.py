from datetime import datetime
from flask import render_template
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_security import Security, login_required, current_user, utils
from flask_login import LoginManager, login_user, logout_user
from models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key

# Configure LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Create a simple user store (replace this with a real database in production)
users = {'KSG': User('KSG', 'piqumisgreat')}  # Replace with your desired username and password

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return "Invalid username or password", 401

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )



@app.route('/game1')
@login_required
def game1():
    """Renders Game 1."""
    return render_template(
        'game1.html',
        title='piQum',
        year=datetime.now().year,
        message='piQum Classic'
    )
@app.route('/game2')
@login_required
def game2():
    """Renders the Game 2."""
    return render_template(
        'game2.html',
        title='Bonus piQum',
        year=datetime.now().year,
        message='Bonus piQum'
    )
@app.route('/game3')
@login_required
def game3():
    """Renders the Game 2."""
    return render_template(
        'game3.html',
        title='piQum Poker',
        year=datetime.now().year,
        message='piQum Poker'
    )

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

