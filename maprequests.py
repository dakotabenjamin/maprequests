from flask import Flask, render_template, redirect, url_for, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, \
    SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import Required, Email
import logging
import sys

app = Flask(__name__)
app.config.from_pyfile('maprequests.cfg')
bootstrap = Bootstrap(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


class MapForm(Form):
    name = StringField('Name:', validators=[Required()])
    email = StringField('Email:', validators=[Required(), Email()])
    pageSize = SelectField(
        'Page Size:',
        choices=[('std', '8.5x11'), ('lg', '11x17')],
        validators=[Required()])
    orientation = RadioField(
        'Page Orientation:',
        choices=[('portrait', 'Portrait'), ('landscape', 'Landscape')],
        validators=[Required()])
    submit = SubmitField('Next')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MapForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['pageSize'] = form.pageSize.data
        session['orientation'] = form.orientation.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
