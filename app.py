from flask import Flask, request

from mail.creator.form import FormData, FormMailCreator
from mail.sender import Mailer
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
email_portfolio = str(os.getenv("email_portfolio"))


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    phone = data['phone']
    email = data['email']
    topic = data['topic']
    text = data['text']

    form_data = FormData(name=name, surname=surname, phone=phone, email=email, topic=topic, text=text)

    mailer = Mailer()
    mailer_creator = FormMailCreator({'mail': email_portfolio}, form_data)
    mailer.send_mail(mailer_creator.recipient, mailer_creator.msg)

    return 'Email sent successfully'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
    # app.run( port=8888, debug=True)
