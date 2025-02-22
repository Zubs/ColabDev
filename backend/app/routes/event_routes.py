from flask import Blueprint, request
from app.controllers.event_controller import EventController

bp = Blueprint('event', __name__, url_prefix='/events')

@bp.route('', methods=['GET'])
def get_events():
    return EventController.get_events(request.args.get('group_by'))

@bp.route('', methods=['POST'])
def create_event():
    return EventController.create_event(request.json)

@bp.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    return EventController.update_event(event_id, request.json)

@bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    return EventController.delete_event(event_id)
