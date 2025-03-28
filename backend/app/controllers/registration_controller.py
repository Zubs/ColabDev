from flask import jsonify
from app.services.registration_service import RegistrationService
from app.controllers.auth_controller import token_required
from postmarker.core import PostmarkClient
import os


class RegistrationController:
    # Initialize Postmark client
    postmark = PostmarkClient(server_token=os.environ.get('POSTMARK_SERVER_TOKEN'))

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

        # Send confirmation email to the registrant
        RegistrationController.send_confirmation_email(registration)

        # Send notification email to admin if configured
        admin_email = os.environ.get('ADMIN_EMAIL')
        if admin_email:
            RegistrationController.send_admin_notification(registration, admin_email)

        # Send notification to carer if carer details are provided
        if "carerDetails" in data and data["carerDetails"].get("email"):
            RegistrationController.send_carer_notification(registration)

        return jsonify({"message": "Registration added successfully", "id": registration.id}), 201

    @classmethod
    def send_confirmation_email(cls, registration):
        """Send a confirmation email to the registrant"""
        try:
            cls.postmark.emails.send(
                From=os.environ.get('EMAIL_FROM', 'noreply@example.com'),
                To=registration.email,
                Subject=f"Registration Confirmation - {registration.event_date}",
                TextBody=f"""
                Dear {registration.title} {registration.first_name} {registration.last_name},

                Thank you for registering for our event on {registration.event_date}.

                Event Details:
                - Date: {registration.event_date}
                - Subject Area: {registration.subject_area}
                - Level of Study: {registration.level_of_study}
                - Number of Guests: {registration.guest_count}

                We are looking forward to seeing you!

                Best regards,
                The Events Team
                """,
                HtmlBody=f"""
                <html>
                <body>
                    <h2>Registration Confirmation</h2>
                    <p>Dear {registration.title} {registration.first_name} {registration.last_name},</p>
                    <p>Thank you for registering for our event on <strong>{registration.event_date}</strong>.</p>

                    <h3>Event Details:</h3>
                    <ul>
                        <li>Date: {registration.event_date}</li>
                        <li>Subject Area: {registration.subject_area}</li>
                        <li>Level of Study: {registration.level_of_study}</li>
                        <li>Number of Guests: {registration.guest_count}</li>
                    </ul>

                    <p>We are looking forward to seeing you!</p>

                    <p>Best regards,<br>
                    The Events Team</p>
                </body>
                </html>
                """
            )
            return True
        except Exception as e:
            # Log the error but don't stop the registration process
            print(f"Error sending confirmation email: {str(e)}")
            return False

    @classmethod
    def send_admin_notification(cls, registration, admin_email):
        """Send a notification email to the admin"""
        try:
            cls.postmark.emails.send(
                From=os.environ.get('EMAIL_FROM', 'noreply@example.com'),
                To=admin_email,
                Subject=f"New Registration - {registration.first_name} {registration.last_name}",
                TextBody=f"""
                A new registration has been submitted:

                Name: {registration.title} {registration.first_name} {registration.last_name}
                Email: {registration.email}
                Phone: {registration.phone_number}
                Event Date: {registration.event_date}
                Subject Area: {registration.subject_area}
                Level of Study: {registration.level_of_study}
                Guest Count: {registration.guest_count}

                Address:
                {registration.address_line1}
                {registration.address_line2}
                {registration.city}, {registration.postcode}
                {registration.country}

                Marketing Sources: {registration.marketing_sources}
                """,
                HtmlBody=f"""
                <html>
                <body>
                    <h2>New Registration</h2>

                    <h3>Registrant Details:</h3>
                    <p>
                        <strong>Name:</strong> {registration.title} {registration.first_name} {registration.last_name}<br>
                        <strong>Email:</strong> {registration.email}<br>
                        <strong>Phone:</strong> {registration.phone_number}<br>
                        <strong>Event Date:</strong> {registration.event_date}<br>
                        <strong>Subject Area:</strong> {registration.subject_area}<br>
                        <strong>Level of Study:</strong> {registration.level_of_study}<br>
                        <strong>Guest Count:</strong> {registration.guest_count}
                    </p>

                    <h3>Address:</h3>
                    <p>
                        {registration.address_line1}<br>
                        {registration.address_line2}<br>
                        {registration.city}, {registration.postcode}<br>
                        {registration.country}
                    </p>

                    <p><strong>Marketing Sources:</strong> {registration.marketing_sources}</p>

                    {f'<h3>Carer Details:</h3><p><strong>Name:</strong> {registration.carer_first_name} {registration.carer_last_name}<br><strong>Email:</strong> {registration.carer_email}</p>' if registration.carer_first_name else ''}
                </body>
                </html>
                """
            )
            return True
        except Exception as e:
            print(f"Error sending admin notification email: {str(e)}")
            return False

    @classmethod
    def send_carer_notification(cls, registration):
        """Send a notification email to the carer if details provided"""
        if not registration.carer_email:
            return False

        try:
            cls.postmark.emails.send(
                From=os.environ.get('EMAIL_FROM', 'noreply@example.com'),
                To=registration.carer_email,
                Subject=f"Event Registration Confirmation for {registration.first_name} {registration.last_name}",
                TextBody=f"""
                Dear {registration.carer_first_name} {registration.carer_last_name},

                This email is to inform you that {registration.first_name} {registration.last_name} has registered for our event on {registration.event_date}.

                Event Details:
                - Date: {registration.event_date}
                - Subject Area: {registration.subject_area}
                - Level of Study: {registration.level_of_study}
                - Number of Guests: {registration.guest_count}

                If you have any questions, please contact us.

                Best regards,
                The Events Team
                """,
                HtmlBody=f"""
                <html>
                <body>
                    <h2>Event Registration Notification</h2>
                    <p>Dear {registration.carer_first_name} {registration.carer_last_name},</p>
                    <p>This email is to inform you that <strong>{registration.first_name} {registration.last_name}</strong> has registered for our event on <strong>{registration.event_date}</strong>.</p>

                    <h3>Event Details:</h3>
                    <ul>
                        <li>Date: {registration.event_date}</li>
                        <li>Subject Area: {registration.subject_area}</li>
                        <li>Level of Study: {registration.level_of_study}</li>
                        <li>Number of Guests: {registration.guest_count}</li>
                    </ul>

                    <p>If you have any questions, please contact us.</p>

                    <p>Best regards,<br>
                    The Events Team</p>
                </body>
                </html>
                """
            )
            return True
        except Exception as e:
            print(f"Error sending carer notification email: {str(e)}")
            return False
