import project_classes.project as PROJECT
from pathlib import PurePath
import uuid

class Solution:
    # header
    sln_ver: str = None
    vs_ver: str = None
    vs_min_ver: str = None
    # file body - solution and project definitions
    projects = []
    # file body - pre- and postSolution definitions
    sln_config_platforms = []   # preSolution
    proj_config_platforms = []  # postSolution
    sln_props = []              # preSolution
    ext_globs = []              # postSolution

    def __init__(self):
        pass

    def loadSolutionFile(self, sln_path: PurePath):
        file = open(sln_path, "r")  ## TODO: try/catch FileNotFoundError

        for line in file:
            # begin list of ifs to check for data we want to extract

            # format version
            if (line.find("Format Version") != -1):  # if found at all
                ver = line.split(" ")[-1]
                try:
                    ver = float(ver)
                    self.sln_ver = ver
                except ValueError:
                    self.sln_ver = -1
                continue
            
            # vs version
            if (line.find("VisualStudioVersion") == 0):  # if found pos is at beginning
                ver_str = line.split(" ")[-1].replace("\n", "")  # get that last word, minus any trailing newlines
                digits = ver_str.split(".")  # get list of decimal numbers, e.g. XX.XX.XXXXX.X

                if (len(digits) == 4):
                    all_digits = True
                    for digit in digits:
                        if (not digit.isdecimal):
                            all_digits = False
                    
                    if (all_digits):
                        self.vs_ver = ver_str
                    else:
                        self.vs_ver = -1  # invalid version
                
                continue
            
            # min vs version
            if (line.find("MinimumVisualStudioVersion") == 0):  # if found pos is at beginning
                ver_str = line.split(" ")[-1].replace("\n", "")  # get that last word, minus any trailing newlines
                digits = ver_str.split(".")  # get list of decimal numbers, e.g. XX.XX.XXXXX.X

                if (len(digits) == 4):
                    all_digits = True
                    for digit in digits:
                        if (not digit.isdecimal):
                            all_digits = False
                    
                    if (all_digits):
                        self.vs_min_ver = ver_str
                    else:
                        self.vs_min_ver = -1  # invalid version
                
                continue
        
            # projects
            if (line.find("Project(\"{") == 0):
                proj_type_str = line[line.find("{")+1:line.find("}")]
                proj_type = None

                # extract uuid
                try:
                    proj_type = uuid.UUID(proj_type_str)
                except ValueError:
                    print("There was an error processing Project with type UUID: " + proj_type_str + "! Badly formed UUID!")
                    continue

                # parse line for segments needed for a project: name, vcxproj path, and uuid
                proj_sgmts = line.split(" = ")

                if (len(proj_sgmts) != 2):
                    print("Invalid definition of project!")
                    continue

                sgmts = proj_sgmts[-1].split(", ")

                if (len(sgmts) != 3):
                    print("Invalid number of project info points!")
                    continue

                proj_name = sgmts[0].replace("\"", "")
                proj_vcxproj_rel_path = sgmts[1].replace("\"", "")
                proj_uuid = uuid.UUID(sgmts[2][1:-2])

                print(proj_uuid)

                # print(f"Processed project of type {proj_type_str} with name {proj_name} and uuid {proj_uuid} and rel path {proj_vcxproj_rel_path}")

                self.projects.append(PROJECT.Project(proj_type, proj_uuid, proj_name, proj_vcxproj_rel_path, sln_path.parent))

                print(self.projects[-1])

                continue

            # TODO: projects.

        file.close()
    
    def __str__(self):
        return f"""Format Version: {self.sln_ver}
VS Version: `{self.vs_ver}`
Min VS Version: `{self.vs_min_ver}`"""
