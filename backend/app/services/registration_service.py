from app.models.registration import Registration
from app import db


class RegistrationService:
    @staticmethod
    def get_all_registrations():
        return Registration.query.all()

    @staticmethod
    def get_registration(registration_id):
        return Registration.query.get(registration_id)

    @staticmethod
    def create_registration(data):
        registration = Registration(
            title=data['title'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            date_of_birth=data['date_of_birth'],
            carer_first_name=data.get('carer_first_name'),
            carer_last_name=data.get('carer_last_name'),
            carer_email=data.get('carer_email'),
            email=data['email'],
            phone_number=data['phone_number'],
            address_line1=data['address_line1'],
            address_line2=data.get('address_line2'),
            city=data['city'],
            postcode=data['postcode'],
            country=data['country'],
            level_of_study=data['level_of_study'],
            subject_area=data['subject_area'],
            event_date=data['event_date'],
            guest_count=data['guest_count'],
            marketing_sources=data['marketing_sources'],
        )
        db.session.add(registration)
        db.session.commit()

        return registration
