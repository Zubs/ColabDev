from flask import Blueprint, request
from app.controllers.auth_controller import AuthController

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    return AuthController.login(request.json)

@bp.route('/logout', methods=['POST'])
def logout():
    return AuthController.logout()

@bp.route('/profile', methods=['GET'])
def get_profile():
    return AuthController.get_profile()

@bp.route('/register', methods=['POST'])
def register():
    return AuthController.register(request.json)
