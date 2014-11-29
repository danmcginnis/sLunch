from flask import Flask,  render_template
from flask.ext.bootstrap import Bootstrap
from app import app

bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
            title='sLunch Calculator')
