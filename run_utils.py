import sys, file_utils

def are_arguments_valid():
    if len(sys.argv) < 2:
        return False
    if len(sys.argv) == 2:
        if not file_utils.verify_directory_path(sys.argv[2]):
            return False
    
    return True