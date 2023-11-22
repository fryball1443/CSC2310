import json

class Contact:
    def __init__(self, first_name, last_name, user_id, email, department, job_title, phone_number, building, po_box):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.email = email
        self.department = department
        self.job_title = job_title
        self.phone_number = phone_number
        self.building = building
        self.po_box = po_box

class Event:
    def __init__(self, event_name, event_id, event_date, start_time, location, duration):
        self.event_name = event_name
        self.event_id = event_id
        self.event_date = event_date
        self.start_time = start_time
        self.location = location
        self.duration = duration

with open('contacts.json') as f:
    contact_data = json.load(f)

contacts = []
for contact in contact_data:
    contacts.append(Contact(contact['FirstName'], contact['LastName'], contact['UID'], contact['EmailAddress'], contact['Dept'], contact['Title'], contact['Phone'], contact['Building'], contact['POBox']))

for contact in contacts:
    print(contact.first_name, contact.last_name, contact.user_id, contact.email, contact.department, contact.job_title, contact.phone_number, contact.building, contact.po_box)

with open('events.json') as g:
    event_data = json.load(g)

events = []
for event in event_data["university_events"]:
    events.append(Event(event['Name'], event['UID'], event['Date'], event['StartTime'], event['Location'], event['Duration']))

for event in events:
    print(event.event_name, event.event_id, event.event_date, event.start_time, event.location, event.duration)

