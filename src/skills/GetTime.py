import datetime

# Get the current time
def GetTime():
    Hrs = int(datetime.datetime.now().hour)
    Mins = int(datetime.datetime.now().minute)
    CTime = f"{Hrs-12}:{Mins} PM" if Hrs >= 13 else f"{Hrs}:{Mins} AM"
    return CTime
