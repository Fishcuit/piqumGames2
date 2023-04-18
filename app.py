from flask import Flask
from datetime import datetime
from flask import render_template

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

if __name__ == '__main__':
    app.run()

