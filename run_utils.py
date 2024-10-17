import sys, file_utils, uuid, os

def are_arguments_valid():
    if len(sys.argv) < 2:
        return False
    if len(sys.argv) == 2:
        if not file_utils.verify_directory_path(sys.argv[1]):
            return False
    
    return True

def get_project_dir_arg():
    if are_arguments_valid():
        return sys.argv[1]

class project_info:
    def __init__(self):
        self.dir = ""
        self.name = ""
        self.main_uuid = ""
        self.project_uuid = ""
        self.header_files = []
        self.resource_files = []
        self.source_files = []
        self.all_files = []
    
    def generate_uuid(self):
        self.project_uuid = str(uuid.uuid4()).upper()
    
    def generate_main_info(self, project_dir, main_uuid):
        self.name = os.path.basename(project_dir.dir)
        self.main_uuid = main_uuid
        self.generate_uuid()

    def generate_file_info(self):
        # get details about categorized files
        header_files, resource_files, source_files = file_utils.categorize_files(self.dir)

        # set file info to info about categorized files
        self.header_files = header_files
        self.resource_files = resource_files
        self.source_files = source_files

        # all files
        self.all_files = self.header_files + self.resource_files + self.source_files
