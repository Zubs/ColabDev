from app.models.event import Event
from app import db

class EventService:
    @staticmethod
    def get_all_events():
        return Event.query.filter_by(public=True).order_by(Event.date.desc(), Event.time.desc()).all()

    @staticmethod
    def create_event(title, description, date, time, duration, location, public=True):
        event = Event(title=title, description=description, date=date, time=time, duration=duration, location=location,
                      public=public)
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def update_event(event_id, title, description, date, time, duration, location):
        event = Event.query.get(event_id)
        if event:
            event.title = title
            event.description = description
            event.date = date
            event.time = time
            event.duration = duration
            event.location = location
            db.session.commit()
        return event

    @staticmethod
    def delete_event(event_id):
        event = Event.query.get(event_id)
        if event:
            db.session.delete(event)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_all_events_grouped_by_date():
        events = Event.query.filter_by(public=True).order_by(Event.date.asc(), Event.time.asc()).all()
        grouped_events = {}
        for event in events:
            date = event.date.strftime('%d/%m/%Y')
            if date not in grouped_events:
                grouped_events[date] = []
            grouped_events[date].append(event)

        return grouped_events

    @staticmethod
    def get_event(event_id):
        return Event.query.get(event_id)
