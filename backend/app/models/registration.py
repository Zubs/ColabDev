from app import db
from datetime import datetime

class Registration(db.Model):
    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    carer_first_name = db.Column(db.String(50), nullable=True)
    carer_last_name = db.Column(db.String(50), nullable=True)
    carer_email = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address_line1 = db.Column(db.String(100), nullable=False)
    address_line2 = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    level_of_study = db.Column(db.String(50), nullable=False)
    subject_area = db.Column(db.String(100), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    marketing_sources = db.Column(db.ARRAY(db.String), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now().astimezone)
    updated_at = db.Column(db.DateTime, default=datetime.now().astimezone, onupdate=datetime.now().astimezone)
