from app.models.faq import FAQ
from app import db

class FAQService:
    @staticmethod
    def get_all_faqs():
        return FAQ.query.filter_by(public=True).order_by(FAQ.updated_at.desc()).all()

    @staticmethod
    def create_faq(question, answer):
        faq = FAQ(question=question, answer=answer)
        db.session.add(faq)
        db.session.commit()
        return faq

    @staticmethod
    def update_faq(faq_id, question, answer):
        faq = FAQ.query.get(faq_id)
        if faq:
            faq.question = question
            faq.answer = answer
            db.session.commit()
        return faq

    @staticmethod
    def delete_faq(faq_id):
        faq = FAQ.query.get(faq_id)
        if faq:
            db.session.delete(faq)
            db.session.commit()
            return True
        return False
