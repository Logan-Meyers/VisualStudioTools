import run_utils, constants
import os, shutil
from pathlib import Path

# Helper to verify directory exists
def verify_directory_path(path_str: str):
    path = Path(path_str)

    if path.exists() and path.is_dir():
        return True
    
    return False

# Helper to move files TO the project folder
# for operation `up`
def move_files_to_project_folder(project_info: run_utils.ProjectInfo):
    # make main project directory
    if not os.path.exists(project_info.proj_dir):
        os.makedirs(project_info.proj_dir)
    
    # move each file
    for file in project_info.all_files:
        old = project_info.root_dir / file
        new = project_info.root_dir / project_info.name / file
        new_parents = new.parent

        # make directories if they don't exist in the new folder
        os.makedirs(new_parents, exist_ok=True)

        # move the file
        shutil.move(old, new)

# Helper to move files TO the project folder
# for operation `down`
def move_files_from_project_folder(project_info: run_utils.ProjectInfo):
    # move each file
    for file in project_info.all_files:
        old = project_info.root_dir / file
        
        try:
            new = project_info.root_dir / (file.relative_to(project_info.name))
        except ValueError:
            # path not subpath of the project folder, skip file
            continue

        new_parents = new.parent

        # make directories if they don't exist in the new folder
        os.makedirs(new_parents, exist_ok=True)

        # move the file
        shutil.move(old, new)

# Helper to remove all .DS_Store files
def remove_DS_Stores(project_info: run_utils.ProjectInfo):
    # find all instances and remove them
    for ds_store_file in Path(project_info.root_dir).rglob('.DS_Store'):
        if ds_store_file.is_file():
            ds_store_file.unlink()
            print(f"Removed .DS_Store file: {ds_store_file}")

# Helper to remove empty folders
def remove_empty_folders(project_info: run_utils.ProjectInfo):
    # straight from ChatGPT
    # Recursively iterate over all directories (bottom-up)
    for folder in sorted(Path(project_info.root_dir).rglob('*'), key=lambda p: len(p.parts), reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):  # Check if the folder is empty
            folder.rmdir()  # Remove the empty folder
            print(f"Removing empty folder {folder}")

def list_empty_folders(project_info: run_utils.ProjectInfo):
    for folder in sorted(Path(project_info.root_dir).rglob('*'), key=lambda p: len(p.parts), reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):  # Check if the folder is empty
            print(f"Empty folder: {folder}")

# Categorize files - RELATIVE
def categorize_files(project_dir):
    source_files = []
    header_files = []
    resource_files = []
    
    for file_path in Path(project_dir).rglob('*'):
        if file_path.is_file():
            if file_path.suffix == '.c':
                source_files.append(file_path.relative_to(project_dir))
            elif file_path.suffix == '.h':
                header_files.append(file_path.relative_to(project_dir))
            else:
                resource_files.append(file_path.relative_to(project_dir))
    
    return header_files, resource_files, source_files

def remove_unnecessary_files(project_info: run_utils.ProjectInfo):
    removed_file_count = 0
    removed_files = []
    for file in project_info.resource_files:
        if file.parts[-1] in constants.DEFAULT_UNNECESSARY_FILES:
            print("Removing file: `{}` because it matches name `{}`".format(file, file.parts[-1]))
            remove_file(project_info.root_dir / file)
            removed_file_count += 1
            removed_files.append(file)
        for ext in constants.DEFAULT_UNNECESSARY_EXTS:
            if file.suffix == ext:
                print("Removing file: `{}` because it matches extension: `{}`".format(file, ext))
                remove_file(project_info.root_dir / file)
                removed_file_count += 1
                removed_files.append(file)
    
    # remove unnecessary files from the resources array in a weird way
    # I was worried about, if I pop()'ed them, the indexes would be off
    tmp_res_files = project_info.resource_files
    project_info.resource_files = []

    for file in tmp_res_files:
        if not file in removed_files:
            project_info.resource_files.append(file)

    project_info.update_all_files()

    print("Removed {} unnecessary files!".format(removed_file_count))

# Abstraction of file writing because `with open` is ugly
def write_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

# Abstraction of file deletion
def remove_file(path):
    os.remove(path)
