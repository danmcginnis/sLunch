from flask import Flask,  render_template
from flask.ext.bootstrap import Bootstrap
from app import app

bootstrap = Bootstrap(app)

title = 'sLunch Calculator'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
            title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
            title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
