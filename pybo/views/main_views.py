from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from .. import db
from ..forms import ContactForm
from ..models import Contact

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def index():
    form = ContactForm()

        if request.method == 'POST' and form.validate_on_submit():
            contact = Contact(name=form.name.data, number=form.number.data, create_date=datetime.now())
            db.session.add(contact)
            db.session.commit()
        return redirect(url_for('main.index'))

    return render_template("index.html", form=form)
