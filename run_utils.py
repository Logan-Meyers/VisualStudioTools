import file_utils, constants
import sys, uuid, pathlib

# determine if arguments entered exist and are valid
def are_arguments_valid():
    # needs at least 2 arguments
    if len(sys.argv) < 2:
        return False
    # make sure directory exists
    if len(sys.argv) >= 2:
        if not file_utils.verify_directory_path(sys.argv[1]):
            return False
    # make sure project type is supported
    if len(sys.argv) >= 3:
        if not sys.argv[2] in constants.VCX_PROJ_TYPES.keys():
            return False
    
    return True

# return the directory arg
def get_project_dir_arg():
    if are_arguments_valid():
        return sys.argv[1]
    
# return the project type arg, with defaults
def get_project_type_arg():
    if are_arguments_valid():
        if len(sys.argv) >= 3:
            return sys.argv[2]
        else:
            return constants.DEFAULT_PROJ_TYPE

# project info class, to hold and abstract data about the project being converted
class project_info:
    def __init__(self):
        self.root_dir = pathlib.Path()
        self.proj_dir = pathlib.Path()
        self.name = ""
        self.proj_type = ""
        self.proj_type_uuid = ""
        self.proj_unique_uuid = ""
        self.header_files = []
        self.resource_files = []
        self.source_files = []
        self.all_files = []    

    def generate_uuid(self):
        self.proj_unique_uuid = str(uuid.uuid4()).upper()
    
    def generate_main_info(self, project_dir: str, project_type: str):
        self.root_dir = pathlib.PurePath(project_dir)
        self.name = self.root_dir.parts[-1]
        self.proj_dir = self.root_dir / self.name
        self.proj_type = project_type
        self.proj_type_uuid = constants.VCX_PROJ_TYPES.get(project_type)
        
        if self.proj_type_uuid == None:
            raise KeyError("Hey! Invalid type of project given!")
        
        self.generate_uuid()

    def generate_file_info(self):
        # get details about categorized files
        hdr, res, src = file_utils.categorize_files(self.root_dir)

        # set file info to info about categorized files
        self.header_files = hdr
        self.resource_files = res
        self.source_files = src

        # all files
        self.all_files = self.header_files + self.resource_files + self.source_files
    
    def display_info(self):
        print(f"""Project Name: {self.name}\
               \n  - Project Root Directory: {self.root_dir}\
               \n  - Project New Directory: {self.proj_dir}\
               \n  - Project Type: {self.proj_type}\
               \n  - Project Type UUID: {{{self.proj_type_uuid}}}\
               \n  - Project Unique UUID: {{{self.proj_unique_uuid}}}\
               \n  - Project Files:\
               \n    - Header Files: {self.header_files}\
               \n    - Resource Files: {self.resource_files}\
               \n    - Source files: {self.source_files}""")
