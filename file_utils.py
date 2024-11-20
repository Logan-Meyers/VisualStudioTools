import run_utils, constants
import os, shutil
from pathlib import Path

# Helper to verify directory exists
def verify_directory_path(path_str: str):
    path = Path(path_str)

    if path.exists() and path.is_dir():
        return True
    
    return False

# Helper to move files to the project folder
def move_files_to_project_folder(project_info: run_utils.ProjectInfo):
    if not os.path.exists(project_info.proj_dir):
        os.makedirs(project_info.proj_dir)
    
    for file in project_info.all_files:
        shutil.move(file, project_info.proj_dir)

# Categorize files
def categorize_files(project_dir):
    source_files = []
    header_files = []
    resource_files = []
    
    for root, _, files in os.walk(project_dir):
        for file in files:
            # print(file)
            if file.endswith('.c'):
                # source_files.append(os.path.join(root, file))
                source_files.append(project_dir / file)
            elif file.endswith('.h'):
                # header_files.append(os.path.join(root, file))
                header_files.append(project_dir / file)
            else:
                # resource_files.append(os.path.join(root, file))
                resource_files.append(project_dir / file)
    
    return header_files, resource_files, source_files

def remove_unnecessary_files(project_info: run_utils.ProjectInfo):
    removed_files = 0
    for file in project_info.resource_files:
        if file.parts[-1] in constants.DEFAULT_UNNECESSARY_FILES:
            print("Removing file: `{}/{}` because it matches name `{}`".format(file.parts[-2], file.parts[-1], file.parts[-1]))
            remove_file(file)
            removed_files += 1
        for ext in constants.DEFAULT_UNNECESSARY_EXTS:
            if file.parts[-1].endswith(ext):
                print("Removing file: `{}/{}` because it matches extension: `{}`".format(file.parts[-2], file.parts[-1], ext))
                remove_file(file)
                removed_files += 1
    
    print("Removed {} unnecessary files!".format(removed_files))

# Abstraction of file writing because `with open`` is ugly
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

# Abstraction of file deletion
def remove_file(path):
    os.remove(path)