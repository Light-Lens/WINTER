import datetime

# Get the today's date
def GetDate():
    return datetime.datetime.today().strftime('%d-%m-%Y')
