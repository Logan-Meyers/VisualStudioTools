import file_utils, constants
import sys, uuid, pathlib

# determine if arguments entered exist and are valid
def are_arguments_valid():
    # needs at least 2 arguments
    if len(sys.argv) < 2:
        return False
    
    # if 2 arguments (.., project path):
    # convert project to default project type
    if len(sys.argv) == 2:
        if not file_utils.verify_directory_path(sys.argv[1]):
            return False
    
    # if >= 3 arguments, check for other combinations
    if len(sys.argv) >= 3:
        first_is_conversion = False
        # check first argument for conversion type
        if sys.argv[1] in constants.OPERATION_TYPES:
            # print("conversion type: {}".format(sys.argv[1]))
            first_is_conversion = True
        # check last argument for path to project
        if not file_utils.verify_directory_path(sys.argv[-1]):
            return False
        # check for other options
        first_index = 2 if first_is_conversion else 1
        for i in range(first_index, len(sys.argv)-1):
            # print("i: {}".format(sys.argv[i]))
            if not sys.argv[i] in constants.ARGUMENT_OPTIONS:
                return False
    
    return True

def make_run_args():
    run_args = RunArgs()

    # if 2 arguments (.., project path):
    # convert project to default project type
    if len(sys.argv) == 2:
        run_args.operation_type = constants.DEFAULT_OPERATION_TYPE
        run_args.project_path = sys.argv[-1]
    
    # if >= 3 arguments, check for other combinations
    if len(sys.argv) >= 3:
        first_is_conversion = False
        # set conversion type
        if sys.argv[1] in constants.OPERATION_TYPES:
            first_is_conversion = True
            run_args.operation_type = sys.argv[1]
        else:
            run_args.operation_type = constants.DEFAULT_OPERATION_TYPE

        # set project path
        run_args.project_path = sys.argv[-1]
        
        # set other args
        first_index = 2 if first_is_conversion else 1
        for i in range(first_index, len(sys.argv)-1):
            run_args.args.append(sys.argv[i])
    
    return run_args

# return the project type from run args
def get_project_type_arg(arg_options):
    for option in arg_options:
        option = option.removeprefix("--")
        if option in constants.VCX_PROJ_TYPES:
            return option
    
    return constants.DEFAULT_PROJ_TYPE

# return conversion type arg
def get_operation_type_arg():
    if sys.argv[1] in constants.OPERATION_TYPES:
        return sys.argv[1]
    else:
        return constants.DEFAULT_OPERATION_TYPE

def print_files_clean(file_type, files):
    print(f"{file_type}")
    for file in files:
        print(f"                          {file}")

# run arg class, holds project path, conversion type, and any arguments passed in
class RunArgs:
    def __init__(self):
        self.operation_type = None
        self.project_path = None
        self.args = []

# project info class, to hold and abstract data about the project being converted
class ProjectInfo:
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
        # get details about categorized files - RELATIVE TO ROOT_DIR
        hdr, res, src = file_utils.categorize_files(self.root_dir)

        # set file info to info about categorized files
        self.header_files = hdr
        self.resource_files = res
        self.source_files = src

        # all files
        self.update_all_files()
    
    def update_all_files(self):
        self.all_files = self.header_files + self.resource_files + self.source_files

    def display_info(self):
        print(f"""Project Name:             {self.name}\
               \n- Project Root Directory: {self.root_dir}\
               \n- Project New Directory:  {self.proj_dir}\
               \n- Project Type:           {self.proj_type}\
               \n- Project Type UUID:      {{{self.proj_type_uuid}}}\
               \n- Project Unique UUID:    {{{self.proj_unique_uuid}}}\
               \n- Project Files:""")
        print_files_clean("  - Header Files:         ", self.header_files)
        print_files_clean("  - Resource Files:       ", self.resource_files)
        print_files_clean("  - Source Files:         ", self.source_files)

def print_usage():
    print()
    print("    python ./main.py [conversion type] [[args]] [project path]")
    print()
    print("Operations:")
    print("    `help`/`usage`: Show this info")
    print("    `up`:           VS Code -> Visual Studio")
    print("    `down`:         VS Code <- Visual Studio")
    print("    `sync`:         Update Visual Studio files if necessary")
    print("    `ls`:           Lists info about your project [redundant, runs anyway]")
    print()
    print("Args:")
    print("    `--arm`: include arm build targets")
    print("    `--remove-unnecessary`: deletes files such as `.vscode` and `makefile`")
    print()