import subprocess, pywhatkit, os

# Open Sites or Apps
def OpenSitesOrApps(appname):
    proc = subprocess.Popen(["powershell", "get-StartApps", appname, "| Select-Object -ExpandProperty AppID"], stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()

    out = out.decode("utf-8")
    out = out.split("\r\n")
    out.pop()

    if out:
        AppID = out[0]
        os.system(f"start explorer shell:appsfolder\{AppID}")

    else: pywhatkit.search(appname)
    return ""
