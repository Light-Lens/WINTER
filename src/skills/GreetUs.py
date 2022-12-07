import datetime

# Greet the user according to the current time.
def GreetUs():
    time_of_the_day = ""
    Hour = int(datetime.datetime.now().hour)

    if Hour >= 0 and Hour < 12: time_of_the_day = "Morning"
    elif Hour >= 12 and Hour < 18: time_of_the_day = "Afternoon"
    elif Hour >= 18 and Hour < 22: time_of_the_day = "Evening"
    elif Hour >= 22 and Hour < 0: time_of_the_day = "Night"
    return time_of_the_day
