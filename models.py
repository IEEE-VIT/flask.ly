import datetime as dt
from app import db


class User:
    # Create the User model which stores their email ID and password
    pass


# Maximum size of original URL is set according to this information:
# https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2000), nullable=False)
    short_url = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=dt.datetime.now)

    def __repr__(self):
        return f"<Url:{self.id}> {self.short_url}"

    def __str__(self):
        return f"{self.short_url}"
