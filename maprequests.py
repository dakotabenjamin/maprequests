from flask import Flask, render_template, redirect, url_for, session
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, \
        SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import Required, Email

app = Flask(__name__)
app.config.from_pyfile('maprequest.cfg')
bootstrap = Bootstrap(app)

class MapForm(Form):
    name = StringField('Name:', validators=[Required()])
    email = StringField('Email:', validators=[Required(), Email()])
    pageSize = SelectField(
            'Page Size:',
            choices=[('std','8.5x11'),('lg','11x17')],
            validators=[Required()])
    orientation = RadioField(
            'Page Orientation:',
            choices=[('portrait','Portrait'),('landscape','Landscape')],
            validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = MapForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['pageSize'] = form.pageSize.data
        session['orientation'] = form.orientation.data
        return redirect(url_for('.mapview', pageSize='std', orientation='portrait'))
    return render_template('index.html', form=form)

@app.route('/mapview', methods=['GET','POST'])
def mapview():
    return render_template('map.html', pageSize='std', orientation='portrait')

if __name__ == '__main__':
    app.run(debug=True)
    submit = SubmitField('Submit')

