import os
from src.skills.OpenSitesOrApps import OpenSitesOrApps

# Create a new project
def CreateProject(proj_name="_git"):
    if proj_name == "_git": OpenSitesOrApps("new github project")
    else:
        dir = f"D:\\Dev Projects\\{proj_name}"

        if not os.path.exists(dir): os.mkdir(dir)

    return ""
