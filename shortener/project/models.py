from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from project import db


class InsertURL:
    def insert(self, url):
        try:
            row = URI_Table.query.order_by(db.desc('index')).first()
            index = row.index
            if index is None:
                index = 0
            else:
                index += 1

            new_url = get_page_id(index=index)

            db.session.add(URI_Table(url=url, s_url=new_url, index=index))
            db.session.commit()
            return new_url
        except:
            return -1

    def result(self, id):
        base_url = 'http://localhost:1338/'
        return base_url + id


class URI_Table(db.Model):
    '''
    url table.
    | ID (INT) | ORIGINAL_URL (STRING)| SHORT_URL (STRING)| INDEX (INT)|
    '''
    __tablename__ = "url"

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(256), unique=True, nullable=False)
    short_url = db.Column(db.String(16), default=True, nullable=False)
    index = db.Column(db.Integer)

    def __init__(self, url: str, s_url: str, index: int):
        self.original_url = url
        self.short_url = s_url
        self.index = index


CHARS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', '_', '~']
CHARS_LEN = len(CHARS)


def get_page_id(index: int):
    result = ''
    q = index // CHARS_LEN
    m = index % CHARS_LEN
    while q > 0:
        result = CHARS[m] + result
        index = q - 1
        q = index // CHARS_LEN
        m = index % CHARS_LEN

    return CHARS[m] + result


class Shortener_Form(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Shorten')
