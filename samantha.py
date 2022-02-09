# This is Sterling's personal scheduler script meant to easily manage and access his calendar with the simple press of a button. Call me Samantha :)


############################
########## SET UP ##########
############################

# Establish Updatable Variables
user = "Sterling"

# Modules
import os
from datetime import datetime
from datetime import date
from this import d
import time
import sys
from tkinter import N

# Define datetime and time variables
today = date.today()
now = datetime.now()


# Define digit-by-digit printing
def delay_print(s):
    #Print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(0.02)


# Path to Schedule Text File
path = "/Users/sterlingmiller/Desktop/Samantha/"
textpath = os.path.join(path, "schedule.txt")


# Initialize an Array Container to hold then count Calendar Events taken from "schedule.txt"
count_list = []


# Initialize an Array Container to store Calendar Events taken from "schedule.txt"
event_list = []


# Initialize current date
date_n = today.strftime(" %m/%d/%y")

# Initialize current time
time_n = now.strftime(" %H:%M:%S")


# Iterate greeting based on time of day
'''
def time_greeting():
    if time_n < "12:00:00":
        x = "morning"
    elif time_n < "05:30:00":
        x = "afternoon"
    elif time_n < "01:00:00":
        x = "evening"
    else:
        x = "hello"
    return x

print(time_greeting)

'''

################################
########## OPERATIONS ##########
################################


### FUNCTIONS ###

# Schedule Item Deletion Function
def schedule_delete(line):
    with open (textpath, 'w') as schedule_txt_wri:
        schedule_txt_wri.truncate(line)


# Have Samantha Greet You Based on what date and time of day it is
  
    # Say Hello to User
delay_print(f'Hello {user}!\n')
time.sleep(0.5)

    # Deliver today's date and the current time
delay_print(f'The date is {date_n}, The time is {time_n}\n')
time.sleep(1)

    # Deliver today's weather conditions
# Use open weather API?


# Create a function that deletes calendar entries that are before today's date (potentially make this a prompt based on a certain conditional [event name, all events with x date, all events before today's date, etc])



# fix final schedule output formatting
''' 
with open(textpath, '+') as textfile:
    # Iterate Every Line in the Text File as an individual Schedule Entry
    for i, line in enumerate(textfile):

        if i == 0:
            header = line.replace(',','')
            continue

        # Split All Parts of Each Schedule Entry Into Individual Components
        split_line = line.rstrip().split(",")
    
    if i[4] < date_n:
        i.remove(line)
    else:
        pass 
    '''


# Streamine this process for the least amount of friction



# Ask if you'd like to add a calendar event

# Sam's Interface & Personality
# if datetime.current_time.hour = 

'''
day_greeting = input()
'''

add_event = str(input("Would you like to add an event to your schedule?: 'y' or 'n' "))
while add_event == "y":
    item1 = input("What is the event?: ")
    item2 = input("what is the focus of your event?: ")
    item0 = input("When do you need to start this assignment?: ")
    item3 = input("How long do you think this assignment will take?: ")
    item4 = input("When is this event or assignment due?: ")
    with open(textpath, 'a') as schedule_txt_app:
        schedule_txt_app.write(f'\n{item0}, {item1}, {item2}, {item3}, {item4}')
    confirmation = print("OK, your event has been added to your calendar :) ")
    more = input("Is there anything else I can do for you?: [add] = Add to my schedule, [view] = View my schedule, [remove] = Remove a schedule event, [n] = cancel ")
    if more == "y" or more == "yes" or more == "Yes" or more == "add" or more == "+":
        pass
    elif more == "view" or more == "v" or more == " " or more == "":
        add_event == "n"
        break
    elif more == "n" or more == "no":
        add_event == "n"
        break
    elif more == "remove" or more == "r" or more == "delete":
        schedule_line_choice = print("Which schedule event(s) would you like to delete?")
        with open (textpath, "r+") as schedule_txt_rw:
            for i, line in enumerate(schedule_txt_rw):
                
                if i == 0:
                    header = line.replace(',','')
                    continue

                 # Split All Parts of Each Schedule Entry Into Individual Components
                split_line = line.rstrip().split(",")

                # Add Each Schedule Entry to our Tuple Container for Reference
                count_list.append(tuple(split_line))

                count = 1
                for event in count_list:
                    event_id = count
                    print(f'{event_id} - {event}')
                    count += 1


### FINISH THIS ###

                # Next list if 
                ask_to_delete = input("Which schedule events would you like to delete? \n (answer example(s): 'number,number,number'; 'number, number, number'; 'number:number') \n choice(s): ")
                colon = ":"
                dash = "-"
                comma = ","
                ampersand = "&"
                semicolon = ";"
                if colon or dash in ask_to_delete:
                    split_line = ask_to_delete.rstrip().split(",")
                    for item in split_line:
                        schedule_delete(item)
                elif comma or ampersand or semicolon in ask_to_delete:
                    d
                

    else:
        add_event == "n"
        break

    
    
########################################
########## INTERNAL FUNCTIONS ##########
########################################


# Open the Textfile
with open(textpath, 'r') as textfile:
    # Iterate Every Line in the Text File as an individual Schedule Entry
    for i, line in enumerate(textfile):

        if i == 0:
            header = line.replace(',','')
            continue

        # Split All Parts of Each Schedule Entry Into Individual Components
        split_line = line.rstrip().split(",")

        # Add Each Schedule Entry to our Tuple Container for Reference
        event_list.append(tuple(split_line))

        # Convert dates strings to datetime variable types


### CONTINUED ISSUE WITH ITERATION AND REMOVAL ONLY OCCURING ON EVERY OTHER LINE ###

# List Comprehension to create new list of filtered non-expired dates

# Single Filtered List Comprehended List
x_date_list = []
for event in event_list:
    if event[4] < date_n:
        x_date_list.append(event)

# print(x_date_list)
# print()

for event in event_list:
    if event in x_date_list:
        event_list.remove(event)

# print(event_list)

# Double Filtered List Comprehended List
xx_date_list = []
for event in event_list:
    split_event = str(event[4]).split("/")
    split_date = date_n.split("/")
    if split_event[2] < split_date[2]:
        xx_date_list.append(event)

# print(xx_date_list)
# print()

for event in event_list:
    if event in xx_date_list:
        event_list.remove(event)

# print(event_list)

# Triple Filtered List Comprehended List
xxx_date_list = []
for event in event_list:
    split_event = str(event[4]).split("/")
    split_date = date_n.split("/")
    if split_event[1] < split_date[1]:
        xxx_date_list.append(event)

# print(xxx_date_list)
# print()

for event in event_list:
    if event in xxx_date_list:
        event_list.remove(event)

# print(event_list)

# Quadrouple Filtered List Comprehended List
xxxx_date_list = []
for event in event_list:
    split_event = str(event[4]).split("/")
    split_date = date_n.split("/")
    if split_event[0] < split_date[0]:
        xxxx_date_list.append(event)

# print(xxxx_date_list)
# print()

for event in event_list:
    if event in xxxx_date_list:
        event_list.remove(event)

# print(event_list)

# Establish new Date List
date_list = [event for event in event_list if event not in xxxx_date_list]

for event in date_list:
    split_event = str(event[4]).split("/")
    split_date = date_n.split("/")
    if split_event[2] < split_date[2]:
        date_list.remove(event)

# print(date_list)

# Event List Updated AS Date List
event_list = date_list

#^# CONTINUED ISSUE WITH ITERATION AND REMOVAL ONLY OCCURING ON EVERY OTHER LINE #^#

def sort_by():
    # Sorting function header
    print(f"SORT OPTIONS:")

    # List of Sort Filters
    sort_list = ["[0] Estimated Starting Date", "[1] Event Name", "[2] Event Focus", "[3] Estimated Total Time Needed", "[4] Due Date"]

    # Print List of Sort Filter Options
    for item in sort_list:
        print(item)

    # User Prompt
    sort_choice = int(input(f"What would you like to sort by?:"))

    def compare(e):
        return e[sort_choice]
        
    return compare
    
myFunc = sort_by()

# Sort Compiled Calendar List by iterating through your event tuples
event_list.sort(key=myFunc)

# Print Header
print(f"\n{header}\n")

# Print Calendar Events in Order
for event in event_list:
    print(event)
    print()

more
