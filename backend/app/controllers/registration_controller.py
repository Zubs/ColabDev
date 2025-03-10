from flask import jsonify
from app.services.registration_service import RegistrationService
from app.controllers.auth_controller import token_required


class RegistrationController:
    @staticmethod
    @token_required
    def get_registrations(user, token):
        registrations = RegistrationService.get_all_registrations()

        return jsonify([{
            "id": registration.id,
            "title": registration.title,
            "first_name": registration.first_name,
            "last_name": registration.last_name,
            "date_of_birth": registration.date_of_birth,
            "carer_first_name": registration.carer_first_name,
            "carer_last_name": registration.carer_last_name,
            "carer_email": registration.carer_email,
            "email": registration.email,
            "phone_number": registration.phone_number,
            "address_line1": registration.address_line1,
            "address_line2": registration.address_line2,
            "city": registration.city,
            "postcode": registration.postcode,
            "country": registration.country,
            "level_of_study": registration.level_of_study,
            "subject_area": registration.subject_area,
            "event_date": registration.event_date,
            "guest_count": registration.guest_count,
            "marketing_sources": registration.marketing_sources,
        } for registration in registrations])

    @staticmethod
    @token_required
    def get_registration(user, token, registration_id):
        registration = RegistrationService.get_registration(registration_id)

        if registration:
            return jsonify({
                "id": registration.id,
                "title": registration.title,
                "first_name": registration.first_name,
                "last_name": registration.last_name,
                "date_of_birth": registration.date_of_birth,
                "carer_first_name": registration.carer_first_name,
                "carer_last_name": registration.carer_last_name,
                "carer_email": registration.carer_email,
                "email": registration.email,
                "phone_number": registration.phone_number,
                "address_line1": registration.address_line1,
                "address_line2": registration.address_line2,
                "city": registration.city,
                "postcode": registration.postcode,
                "country": registration.country,
                "level_of_study": registration.level_of_study,
                "subject_area": registration.subject_area,
                "event_date": registration.event_date,
                "guest_count": registration.guest_count,
                "marketing_sources": registration.marketing_sources,
            })

        return jsonify({"error": "Registration not found"}), 404

    @staticmethod
    def create_registration(data):
        if not data:
            return jsonify({"error": "Invalid data"}), 400

        required_fields = {
            'personalDetails': ['title', 'firstName', 'lastName', 'dateOfBirth'],
            'contactDetails': {
                'email': [],
                'phoneNumber': [],
                'address': ['line1', 'line2', 'city', 'postcode', 'country']
            },
            'courseInterest': ['levelOfStudy', 'subjectArea'],
            'eventDetails': ['date', 'guestCount', 'marketingSources']
        }

        for field, subfields in required_fields.items():
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400
            if isinstance(subfields, dict):
                for subfield, subsubfields in subfields.items():
                    if subfield not in data[field]:
                        return jsonify({"error": f"'{subfield}' in '{field}' is required"}), 400
                    for subsubfield in subsubfields:
                        if subsubfield not in data[field][subfield]:
                            return jsonify({"error": f"'{subsubfield}' in '{subfield}' in '{field}' is required"}), 400
            else:
                for subfield in subfields:
                    if subfield not in data[field]:
                        return jsonify({"error": f"'{subfield}' in '{field}' is required"}), 400

        registration_data = {
            "title": data["personalDetails"]["title"],
            "first_name": data["personalDetails"]["firstName"],
            "last_name": data["personalDetails"]["lastName"],
            "date_of_birth": data["personalDetails"]["dateOfBirth"],
            "email": data["contactDetails"]["email"],
            "phone_number": data["contactDetails"]["phoneNumber"],
            "address_line1": data["contactDetails"]["address"]["line1"],
            "address_line2": data["contactDetails"]["address"]["line2"],
            "city": data["contactDetails"]["address"]["city"],
            "postcode": data["contactDetails"]["address"]["postcode"],
            "country": data["contactDetails"]["address"]["country"],
            "level_of_study": data["courseInterest"]["levelOfStudy"],
            "subject_area": data["courseInterest"]["subjectArea"],
            "event_date": data["eventDetails"]["date"],
            "guest_count": data["eventDetails"]["guestCount"],
            "marketing_sources": data["eventDetails"]["marketingSources"]
        }

        if "carerDetails" in data:
            registration_data["carer_first_name"] = data["carerDetails"]["firstName"]
            registration_data["carer_last_name"] = data["carerDetails"]["lastName"]
            registration_data["carer_email"] = data["carerDetails"]["email"]

        registration = RegistrationService.create_registration(registration_data)

        return jsonify({"message": "Registration added successfully", "id": registration.id}), 201
