from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

app.config['SECRET_KEY'] = 'a35920c20497b3ef12af83126cccab7f'


posts = [
    {
        'author': 'Tour Operator 1',
        'title': 'France',
        'content': '12 Available',
        'date_posted': 'November 13 2018'
    },
    {
        'author': 'Tour Operator 2',
        'title': 'Italy',
        'content': 'Sold Out',
        'date_posted': 'December 3 2018'
    },
    {
        'author': 'Tour Operator 3',
        'title': 'Japan',
        'content': '174 Available',
        'date_posted': 'July 15 2019'
    },
    {
        'author': 'Tour Operator 4',
        'title': 'USA',
        'content': '3 Available',
        'date_posted': 'October 3 2019'
    },
    {
        'author': 'Tour Operator 5',
        'title': 'Cuba',
        'content': 'Sold Out',
        'date_posted': 'January 3 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)