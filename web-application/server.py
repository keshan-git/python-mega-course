from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'pstgressql://postgres;postgres@localhost/db'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        height = request.form['height']
        print(email)
        print(height)

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()

            count = db.session.query(Data.height).count()

            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)

            send_email(email, height, count, average_height)
    return render_template('success.html')


def send_email(email, height, count, average_height):
    from_email = ''
    from_password = ''

    message = '{}'.format(height)

    msg = MIMEText(message, 'html')
    msg['Subject'] = ''
    msg['To'] = email
    msg['From'] = ''

    smtp = smtplib.SMTP('smtp.gamil.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(from_email, from_password)
    smtp.send_message(msg)


if __name__ == '__main__':
    app.run(debug=True, port='8080')