from flask import Blueprint, request
from app.controllers.auth_controller import AuthController

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    return AuthController.login(request.json)

@bp.route('/logout', methods=['POST'])
def logout():
    return AuthController.logout()

@bp.route('/users', methods=['GET'])
def get_profiles():
    return AuthController.get_profiles()

@bp.route('/register', methods=['POST'])
def register():
    return AuthController.register(request.json)
