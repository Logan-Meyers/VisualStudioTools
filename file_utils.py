import run_utils
import os, shutil
from pathlib import Path

# Helper to verify directory exists
def verify_directory_path(path_str: str):
    path = Path(path_str)

    if path.exists() and path.is_dir():
        return True
    
    return False

# Helper to move files to the project folder
def move_files_to_project_folder(project_info: run_utils.project_info):
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

# Abstraction of file writing because `with open`` is ugly
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
