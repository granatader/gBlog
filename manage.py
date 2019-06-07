from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/gblo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))


# generate_password_hash(password, method=pbkdf2:sha1, salt_length=8):
    def __repr__(self):
        return self.name


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run(debug=True)

