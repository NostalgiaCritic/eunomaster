from flask import Blueprint, render_template, request, url_for, current_app
from werkzeug.utils import redirect

from .. import db
from ..forms import ContactForm
from ..models import Contact
import smtplib, ssl
from datetime import datetime
from email.message import EmailMessage

bp = Blueprint('main', __name__, url_prefix='/')

port = 587  # For starttls
smtp_server = "smtp.naver.com"
sender_email = "hyunmin@hagunlab.com"
id = "gusals0702"
password = "xlavhxmfltm54$"

current_app.config['MAIL_SERVER'] = smtp_server
current_app.config['MAIL_PORT'] = port
current_app.config['MAIL_USERNAME'] = sender_email
current_app.config['MAIL_PASSWORD'] = password
current_app.config['MAIL_USE_TLS'] = False
current_app.config['MAIL_USE_SSL'] = True

@bp.route('/', methods=('GET', 'POST'))
def index():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        contact = Contact(name=form.name.data, number=form.number.data, create_date=datetime.now())
        db.session.add(contact)
        db.session.commit()

        senders = 'gusals0702@naver.com'
        # senders = ['gusals0702@naver..com']
        receiver = ['wasse125@naver.com']
        # receiver = 'wasse125@naver.com'
        name = request.form['name']
        number = request.form['number']

        send_email(senders, receiver, name, number)

        return redirect(url_for('main.index'))

    return render_template("index.html", form=form)

def send_email(senders, receiver, name, number):
    try:
        context = ssl.create_default_context()

        message = "신청자 :" + name + ", 번호:" + number

        em = EmailMessage()
        em.set_content(message)
        em['To'] = ", ".join(receiver)
        em['Subject'] = "TEST"
        em['From'] = senders

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(id, password)
            server.send_message(em)
            server.close()

    except Exception as err:
        print(err)
    finally:
        pass