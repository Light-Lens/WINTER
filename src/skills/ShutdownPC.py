import os

# shutdown /s -> shuts down the computer [but it takes time],
# also shows message windows is going to be shutdown within a minute,
# to avoid this we use /t parameter time = 0 seconds /t0, command = shutdown /s /t0, execute to the shell.
# https://stackoverflow.com/a/67342911/18121288
def ShutdownPC():
    os.system("shutdown /s /t0")
    return ""
