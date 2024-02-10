"""
This script fetches upcoming Python events from the official Python website and
prints out a dictionary of event times and corresponding event names.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure Chrome options
options = webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)

# Initialize Chrome driver with options
driver = webdriver.Chrome(options=options)

# Open Python.org website
driver.get('https://www.python.org/')

# Dictionary to store events
events = {}

# Find elements corresponding to event names
event_name_objects = driver.find_elements(By.CSS_SELECTOR, 'ul > li > a[href^="/events/python"]')[:-4]

# Extract event names
event_name = [name.text for name in event_name_objects]

# Remove empty strings from the list
event_name = list(filter(None, event_name))

# Find elements corresponding to event times
time_event_objects = driver.find_elements(By.TAG_NAME, 'time')[5:]

# Extract event times
time_event_serial = [time.text for time in time_event_objects]

# Map event times to event names in the dictionary
for time, event in zip(time_event_serial, event_name):
    events[time] = event

# Print the dictionary of events
print(events)

# Close the browser
driver.quit()
