from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend communication I DON'T KNOW WHAT THIS IS 

# SQLite Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faqs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model for all the  FAQs
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(1000), nullable=False)

#  database tables
with app.app_context():
    db.create_all()

# Route to GET all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return jsonify([{"id": faq.id, "question": faq.question, "answer": faq.answer} for faq in faqs])

# Route to add/POST a new FAQ
@app.route('/faqs', methods=['POST'])
def add_faq():
    data = request.json
    new_faq = FAQ(question=data['question'], answer=data['answer'])
    db.session.add(new_faq)
    db.session.commit()
    return jsonify({"message": "FAQ added successfully"}), 201

# Route to update/PUT an existing FAQ
@app.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    data = request.json
    faq = FAQ.query.get(id)
    if faq:
        faq.question = data['question']
        faq.answer = data['answer']
        db.session.commit()
        return jsonify({"message": "FAQ updated successfully"})
    return jsonify({"error": "FAQ not found"}), 404

# Route to delete an FAQ
@app.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    faq = FAQ.query.get(id)
    if faq:
        db.session.delete(faq)
        db.session.commit()
        return jsonify({"message": "FAQ deleted successfully"})
    return jsonify({"error": "FAQ not found"}), 404

# Run the app here
if __name__ == '__main__':
    app.run(debug=True)
