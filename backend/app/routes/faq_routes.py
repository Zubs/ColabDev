from flask import Blueprint, request
from app.controllers.faq_controller import FAQController

bp = Blueprint('faq', __name__, url_prefix='/faqs')

@bp.route('', methods=['GET'])
def get_faqs():
    return FAQController.get_faqs()

@bp.route('/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    return FAQController.get_faq(faq_id)

@bp.route('', methods=['POST'])
def create_faq():
    return FAQController.create_faq(request.json)

@bp.route('/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    return FAQController.update_faq(faq_id, request.json)

@bp.route('/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    return FAQController.delete_faq(faq_id)
