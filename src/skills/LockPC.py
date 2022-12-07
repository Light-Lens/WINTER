import ctypes

# This function has the same result as pressing Ctrl+Alt+Del and clicking Lock Workstation.
# https://stackoverflow.com/a/20733443/18121288
def LockPC():
    ctypes.windll.user32.LockWorkStation()
    return ""
