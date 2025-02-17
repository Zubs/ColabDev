from flask import jsonify
from app.services.auth_service import AuthService

class AuthController:
    @staticmethod
    def login(data):
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Invalid data"}), 400

        user = AuthService.login(data['username'], data['password'])

        if user:
            return jsonify({"message": "Login successful", "user": user.serialize()}), 200

        return jsonify({"error": "Invalid username or password"}), 401

    @staticmethod
    def logout():
        if AuthService.logout():
            return jsonify({"message": "Logout successful"}), 200

        return jsonify({"error": "No active session"}), 400
