from flask import Flask,  render_template
from flask.ext.bootstrap import Bootstrap
from app import app
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import Required

#app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

title = 'sLunch Calculator'

@app.route('/dan')
def dan():
    return "hello"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    return render_template('index.html',
            title=title,
            form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
            title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(Form):
    TotalBill = DecimalField('What is the total bill?', validators=[Required()])
    TotalPeople = DecimalField('How many people are there?', validators=[Required()]) 

    submit = SubmitField('Submit')