import json
import time

"""
with open('contacts.json') as f:
    data = json.load(f)

for x in data:
    for key, value in x.items():
        print(key, ':', value)
    print()

time.sleep(1) # wait 1 seconds

with open('events.json') as f:
    data = json.load(f)

for x in data:
    for key, value in x.items():
        print(key, ':', value)
    print()
"""

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
    first_name = contact['first_name']
    last_name = contact['last_name']
    user_id = contact['user_id']
    email = contact['email']
    department = contact['department']
    job_title = contact['job_title']
    phone_number = contact['phone_number']
    building = contact['building']
    po_box = contact['po_box']
    contacts.append(Contact(first_name, last_name, user_id, email, department, job_title, phone_number, building, po_box))

for contact in contacts:
    print("Contact:")
    print("First Name:", contact.first_name)
    print("Last Name:", contact.last_name)
    print("User ID:", contact.user_id)
    print("Email:", contact.email)
    print("Department:", contact.department)
    print("Job Title:", contact.job_title)
    print("Phone Number:", contact.phone_number)
    print("Building:", contact.building)
    print("Post Office Box:", contact.po_box)
    print()

time.sleep(1) # wait 1 second

with open('events.json') as f:
    event_data = json.load(f)

events = []
for event in event_data:
    event_name = event['event_name']
    event_id = event['event_id']
    event_date = event['event_date']
    start_time = event['start_time']
    location = event['location']
    duration = event['duration']
    events.append(Event(event_name, event_id, event_date, start_time, location, duration))


for event in events:
    print("Event:")
    print("Event Name:", event.event_name)
    print("Event ID:", event.event_id)
    print("Event Date:", event.event_date)
    print("Start Time:", event.start_time)
    print("Location:", event.location)
    print("Duration:", event.duration)
    print()
