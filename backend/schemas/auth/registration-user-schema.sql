-- DATABASE SCHEMAS FOR RESGISTRATTION

-- 1. REGISTRATON
CREATE TABLE registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(15), -- Constrainted the value to 15 for now.
    date_of_birth DATE,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);


-- 2. EXAMPLE USAGE:
INSERT INTO registrations (event_id,first_name, last_name, email, mobile_number, date_of_birth, country)
VALUES (1, 'Doe', 'john.doe@example.com', '555-1234', '2000-05-20', 'United Kingdom');


-- 3. Querying/ the Registration Data.
SELECT 
    r.registration_id,
    r.first_name,
    r.last_name,
    r.email,
    r.mobile_number,
    r.date_of_birth,
    r.country,
    e.event_name,
    e.event_date,
    e.start_time,
    e.end_time,
    r.created_at
FROM 
    registrations r
JOIN 
    events e ON r.event_id = e.event_id;

-- 4. CREAT a view Table for Registration
CREATE VIEW registration_details AS
SELECT 
    r.registration_id,
    r.first_name,
    r.last_name,
    r.email,
    r.mobile_number,
    r.date_of_birth,
    r.country,
    r.created_at,
    e.event_name,
    e.event_date,
    e.start_time,
    e.end_time
FROM registrations r
JOIN events e ON r.event_id = e.event_id;

-- For example, to retrieve all registration details along with event information, run:
SELECT * FROM registration_details;

--  5. Create a view called single_registration_detail 

CREATE VIEW single_registration_detail AS
SELECT 
    r.registration_id,
    r.first_name
    r.last_name,
    r.email,
    r.mobile_number,
    r.date_of_birth,
    r.country,
    r.created_at,
    e.event_name,
    e.event_date,
    e.start_time,
    e.end_time
FROM registrations r
JOIN events e ON r.event_id = e.event_id;

-- if you want to see the details for a single registration, simply query the view with a filter. 
-- For example, to view the registration with an ID of 5:
SELECT * 
FROM single_registration_detail 
WHERE registration_id = 5;



-- 5. Updating a Registration.
UPDATE registrations
SET mobile_number = '555-6789'
WHERE registration_id = 1;

-- 6. EXAMPLE USAGE to remove from registration.
DELETE FROM registrations
WHERE registration_id = 1;
