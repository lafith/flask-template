from app import app
from flask import render_template
from app.api import say_hello

@app.route('/')
@app.route('/index')
def index():
    """View function for index page"""
    w = say_hello()
    return render_template('index.html', w=w )


