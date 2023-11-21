import json
import time

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


