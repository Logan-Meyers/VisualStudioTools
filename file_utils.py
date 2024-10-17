import os, shutil, run_utils
from pathlib import Path

# Helper to verify directory exists
def verify_directory_path(path_str: str):
    path = Path(path_str)

    if path.exists() and path.is_dir():
        return True
    
    return False

# Helper to move files to the project folder
def move_files_to_project_folder(project_info: run_utils.project_info):
    new_project_dir = os.path.join(project_info.dir, project_info.name)
    
    if not os.path.exists(new_project_dir):
        os.makedirs(new_project_dir)
    
    for file in project_info.all_files:
        shutil.move(file, new_project_dir)

    return new_project_dir

# Categorize files
def categorize_files(project_dir):
    source_files = []
    header_files = []
    resource_files = []
    
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.c'):
                source_files.append(os.path.join(root, file))
            elif file.endswith('.h'):
                header_files.append(os.path.join(root, file))
            else:
                resource_files.append(os.path.join(root, file))
    
    return header_files, resource_files, source_files

# Abstraction of file writing because with open is ugly
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)