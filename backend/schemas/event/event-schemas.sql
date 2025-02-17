-- THE DATEBASE SCHEMAS FOR EVENTS 

-- 1. EVENT CREATION 
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


-- 8. EXAMPLE USAGE: 
INSERT INTO events (event_name, event_date, start_time, end_time)
VALUES
('Undergraduate On Campus Open Day: Morning Session', '2025-03-15', '11:00:00', '15:00:00'),
('Undergraduate On Campus Open Day: Afternoon Session', '2025-03-15', '15:00:00', '18:00:00');

-- 9. Updating an Event
UPDATE events
SET event_name = 'Undergraduate On Campus Open Day: Updated Morning Session',
    start_time = '10:30:00',
    end_time = '14:30:00'
WHERE event_id = 1;

-- 10. Optional: Audit Table for Event Updates,
--  Audit Table for Event Updates.
CREATE TABLE event_updates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    changed_field VARCHAR(100) NOT NULL,
    old_value VARCHAR(255),
    new_value VARCHAR(255),
    updated_by VARCHAR(100), -- Could store the username or ID of the user making the change.
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Usage example: After updating an event, you might insert records into this table.
--  For example, if you updated the event_name, you could run:

-- EXAMPLE USAGE:
INSERT INTO event_updates (event_id, changed_field, old_value, new_value, updated_by)
VALUES (1, 'event_name', 'Undergraduate On Campus Open Day: Morning Session', 
        'Undergraduate On Campus Open Day: Updated Morning Session', 'admin_user');

--NB: This audit log provides a clear history of changes made to each event.

