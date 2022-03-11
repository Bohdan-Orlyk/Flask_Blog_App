from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FlaskApp.db'
db = SQLAlchemy(app)

class Article(db.Model):
    pass


# @app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"User page: {name} - {id}"


if __name__ == "__main__":
    app.run(debug=True)