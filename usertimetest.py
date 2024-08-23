from datetime import datetime # importing py functions

# Grabs current datetime from user and stores in variable now
now = datetime.now()

# Prints current date/time
print("User date and time:", now)

# Converts military time to non-military time and store in formatted_time
formatted_time = now.strftime("%I:%M:%S %p")
print("Formatted non-military time:", formatted_time)

current_hour = now.strftime("%I") #12 hour format
current_period = now.strftime("%p") 

current_hour = int(current_hour) #Extracts as AM or PM

# Nighttime is 8pm to 3:59am
if (current_period == "PM" and current_hour >= 8) or (current_period == "AM" and current_hour < 4):
    time_of_day = "Night"
elif current_period == "AM" and 4 <= current_hour < 10: # Morning is 4am to 9:59am
    time_of_day = "Morning"
else: # Afternoon is 10am to 7:59pm
    time_of_day = "Afternoon"

print(time_of_day)