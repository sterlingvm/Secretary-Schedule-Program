from datetime import datetime
from datetime import date
import os

today = date.today()
time_now = datetime.now()
print(f'{today}{time_now}')


# Define datetime and time variables
today = date.today()
now = datetime.now()

# Initialize current date
date_n = today.strftime("%d/%m/%y")

# Initialize current time
time_n = now.strftime("%H:%M:%S")

date_n > date.strftime("2018", "02", "19")