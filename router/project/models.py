from project import db


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

    @staticmethod
    def is_initialized():
        try:
            uri = URI_Table.query.filter_by(short_url='a').first()
            if uri:
                return True

            return False

        except:
            return False
