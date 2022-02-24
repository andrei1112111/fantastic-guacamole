import datetime

from flask import Flask, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():

    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db = db_session.create_session()
    return render_template("index.html", jobs=db.query(Jobs).all())


if __name__ == '__main__':
    main()
