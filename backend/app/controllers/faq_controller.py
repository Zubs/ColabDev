from flask import jsonify
from app.services.faq_service import FAQService

class FAQController:
    @staticmethod
    def get_faqs():
        faqs = FAQService.get_all_faqs()

        return jsonify([{
            "id": faq.id,
            "question": faq.question,
            "answer": faq.answer
        } for faq in faqs])

    @staticmethod
    def create_faq(data):
        if not data or 'question' not in data or 'answer' not in data:
            return jsonify({"error": "Invalid data"}), 400

        faq = FAQService.create_faq(data['question'], data['answer'])

        return jsonify({"message": "FAQ added successfully", "id": faq.id}), 201

    @staticmethod
    def update_faq(faq_id, data):
        faq = FAQService.update_faq(faq_id, data['question'], data['answer'])

        if faq:
            return jsonify({"message": "FAQ updated successfully"})

        return jsonify({"error": "FAQ not found"}), 404

    @staticmethod
    def delete_faq(faq_id):
        if FAQService.delete_faq(faq_id):
            return jsonify({"message": "FAQ deleted successfully"})

        return jsonify({"error": "FAQ not found"}), 404
