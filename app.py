from flask import Flask
from datetime import datetime
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/game1')
def game1():
    """Renders the about page."""
    return render_template(
        'game1.html',
        title='piQum',
        year=datetime.now().year,
        message='piQum Classic'
    )

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

