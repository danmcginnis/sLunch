from flask import Flask,  render_template
from flask.ext.bootstrap import Bootstrap
from app import app
from flask.ext.wtf import Form
from wtforms import SubmitField, DecimalField
from wtforms.validators import Required

#app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

title = 'sLunch Calculator'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    totalBill = 0
    totalPeople = 0
    perPerson = 0
    form = BillForm()
    if form.validate_on_submit():
        totalBill = form.TotalBill.data
        form.TotalBill.data = ''
        totalPeople = form.TotalPeople.data
        form.TotalPeople.data = ''
        perPerson = totalBill / totalPeople
    return render_template('index.html',
            title=title,
            form=form,
            totalBill = totalBill,
            totalPeople = totalPeople,
            perPerson = perPerson)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',
            title=title), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class BillForm(Form):
    TotalBill = DecimalField('What is the total bill?', validators=[Required()])
    TotalPeople = DecimalField('How many people are there?', validators=[Required()]) 

    submit = SubmitField('Submit')