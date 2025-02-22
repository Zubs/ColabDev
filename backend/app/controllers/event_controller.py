import re
from datetime import datetime
from flask import jsonify
from app.services.event_service import EventService


class EventController:
    @staticmethod
    def get_events():
        try:
            events = EventService.get_all_events()
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify([{
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "date": event.date,
            "time": event.time,
            "duration": event.duration,
            "location": event.location,
            "public": event.public
        } for event in events])

    @staticmethod
    def create_event(data):
        validation_error = EventController.validate_event_data(data)
        if validation_error:
            return validation_error

        try:
            event = EventService.create_event(
                data['title'],
                data['description'],
                datetime.strptime(data['date'], '%d/%m/%Y'),
                datetime.strptime(data['time'], '%H:%M').time(),
                data['duration'],
                data['location']
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify({"message": "Event added successfully", "id": event.id}), 201

    @staticmethod
    def update_event(event_id, data):
        validation_error = EventController.validate_event_data(data)
        if validation_error:
            return validation_error

        try:
            event = EventService.update_event(
                event_id,
                data['title'],
                data['description'],
                datetime.strptime(data['date'], '%d/%m/%Y'),
                datetime.strptime(data['time'], '%H:%M').time(),
                data['duration'],
                data['location']
            )
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        if event:
            return jsonify({"message": "Event updated successfully"})

        return jsonify({"error": "Event not found"}), 404

    @staticmethod
    def delete_event(event_id):
        try:
            if EventService.delete_event(event_id):
                return jsonify({"message": "Event deleted successfully"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify({"error": "Event not found"}), 404

    @staticmethod
    def validate_event_data(data):
        required_fields = ['title', 'description', 'date', 'time', 'duration', 'location']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' is required"}), 400

        try:
            datetime.strptime(data['date'], '%d/%m/%Y')
        except ValueError:
            return jsonify({"error": "Invalid date format, should be DD/MM/YYYY"}), 400

        if not re.match(r'^\d{2}:\d{2}$', data['time']):
            return jsonify({"error": "Invalid time format, should be HH:MM"}), 400

        return None
