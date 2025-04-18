from pathlib import PurePath
import uuid

class Solution:
    # header
    sln_ver = None
    vs_ver = None
    vs_min_ver = None
    # file body - solution and project definitions
    solution_type = None
    project_names = []
    project_paths = []
    project_unique_uuids = []
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
        
            # project solution type UUID
            if (line.find("Project(\"{") == 0):
                sln_uuid_str = line[line.find("{")+1:line.find("}")]

                try:
                    self.solution_type = uuid.UUID(sln_uuid_str)
                except ValueError:
                    self.solution_type = -1  # badly formed UUID
                    
                continue

            # TODO: projects.

        file.close()
    
    def __str__(self):
        return f"""Format Version: {self.sln_ver}
VS Version: `{self.vs_ver}`
Min VS Version: `{self.vs_min_ver}`

Solution UUID: `{self.solution_type}`"""
