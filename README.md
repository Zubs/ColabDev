# Collaborative Development
## Topic: An Undergraduate Open-Day Companion App

## Company Background
The University of Wolverhampton is a leading modern university with a tradition of providing opportunity and academic excellence dating back nearly 200 years.

## Features/Requirements (To-dos)
- [ ] [Landing page](https://www.wlv.ac.uk/news-and-events/open-day/undergraduate-open-day/)
    - [ ] ChatBot
    - [ ] Plenty links including YouTube plugin
    - [ ] Open day guide
- [ ] Admin
    - [ ] Dashboard
        - [x] Events
            - [x] Adding events
            - [x] Viewing events
            - [x] Updating/managing events
            - [x] Removing/deleting events
        - [x] FAQs
            - [x] Adding FAQs
            - [x] Viewing FAQs
            - [x] Updating/managing FAQs
            - [x] Removing/deleting FAQs
        - [ ] Directions
            - [ ] Adding directions
            - [ ] Viewing directions
            - [ ] Updating directions
            - [ ] Deleting directions
        - [ ] Attendance/Engagements
            - [x] View registration details
            - [ ] View single registration detail
            - [ ] How many visitors scanned a given QR Code
    - [ ] Authentication
        - [x] Login
        - [x] Logout
        - [ ] Forgot Password
        - [ ] Reset Password
        - [x] Add New Admin
- [ ] Clients (Users)
    - [x] [Registration form] (https://join.wlv.ac.uk/form/openday?event_id=1712)
    - [x] View programmes listing
        - [ ] View single programme
    - [ ] [Open days] (https://www.wlv.ac.uk/news-and-events/open-day/)
    - [ ] Directions/Maps?
        - [ ] Find your campus and programme
        - [ ] Where to find your program
        - [ ] How to get to us via public transport
        - [ ] Where to park at our open days
        - [ ] Campus maps
            - [ ] Wolverhampton city campus
            - [ ] Walsall campus
            - [ ] Springfield campus
            - [ ] Telford campus
    - [x] FAQs
- [ ] Notifications
    - [ ] Mails (Mailchimp)
        - [ ] Registration confirmation mail
        - [ ] Programme reminders
    - [ ] Push (Firebase)
        - [ ] Programme reminders
    - [ ] SMS (Twillio)
        - [ ] Programme reminders
- [ ] QR Code
    - [ ] Generation for registration confirmation email

## Schemas (drafts)
- Events
- FAQs
- Registrations
- Tokens (JWT)
- Users (Admins)

## Stacks
- [Frontend](./frontend/README.md)
- [Backend](./backend/README.md)
