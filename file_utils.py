import os, shutil
from pathlib import Path

# Helper to verify directory exists
def verify_directory_path(path_str: str):
    path = Path(path_str)

    if path.exists():
        if path.is_dir():
            return True
    
    return False

# Helper to move files to the project folder
def move_files_to_project_folder(source_files, header_files, resource_files, project_name, project_dir):
    new_project_dir = os.path.join(project_dir, project_name)
    
    if not os.path.exists(new_project_dir):
        os.makedirs(new_project_dir)
    
    for file in source_files + header_files + resource_files:
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
    
    return source_files, header_files, resource_files