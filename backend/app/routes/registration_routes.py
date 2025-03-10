from flask import Blueprint, request
from app.controllers.registration_controller import RegistrationController

bp = Blueprint('registration', __name__, url_prefix='/registration')

@bp.route('', methods=['GET'])
def get_registrations():
    return RegistrationController.get_registrations()

@bp.route('/<int:registration_id>', methods=['GET'])
def get_registration(registration_id):
    return RegistrationController.get_registration(registration_id)

@bp.route('', methods=['POST'])
def create_registration():
    return RegistrationController.create_registration(request.json)
