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

def view_contacts():
    for contact in contacts:
        print(contact.first_name, contact.last_name, contact.user_id, contact.email, contact.department, contact.job_title, contact.phone_number, contact.building, contact.po_box)

def view_events():
    for event in events:
        print(event.event_name, event.event_id, event.event_date, event.start_time, event.location, event.duration)

def input_last_communication_date():
    user_id = input("Enter the user ID of the contact: ")
    for contact in contacts:
        if contact.user_id == user_id:
            last_communication_date = input("Enter the last date of communication: ")
            # Update the contact object with the last communication date
            contact.last_communication_date = last_communication_date
            break
    else:
        print("Contact not found.")

def associate_action_items():
    event_id = input("Enter the event ID: ")
    for event in events:
        if event.event_id == event_id:
            action_items = input("Enter the action items (separated by commas): ").split(",")
            # Update the event object with the action items
            event.action_items = action_items
            break
    else:
        print("Event not found.")

def menu():
    while True:
        print("Menu:")
        print("1. View contacts")
        print("2. View events")
        print("3. Input last date of communication for a contact")
        print("4. Associate action items with an event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_contacts()
        elif choice == "2":
            view_events()
        elif choice == "3":
            input_last_communication_date()
        elif choice == "4":
            associate_action_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

with open('contacts.json') as f:
    contact_data = json.load(f)

contacts = []
for contact in contact_data:
    contacts.append(Contact(contact['FirstName'], contact['LastName'], contact['UID'], contact['EmailAddress'], contact['Dept'], contact['Title'], contact['Phone'], contact['Building'], contact['POBox']))

with open('events.json') as g:
    event_data = json.load(g)

events = []
for event in event_data["university_events"]:
    events.append(Event(event['Name'], event['UID'], event['Date'], event['StartTime'], event['Location'], event['Duration']))

while True:
    menu()