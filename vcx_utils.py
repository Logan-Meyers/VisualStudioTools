import file_utils, run_utils, constants
import os
from pathlib import Path

# Create the solution file, including basic information like:
# - Visual Studio version
# - Project name
# - vcxproj location
# - UUIDs
# - build options
def create_sln(project_info: run_utils.ProjectInfo):
    sln_content = constants.SLN_TEMPLATE.format(PROJ_TYPE_UUID=project_info.proj_type_uuid,
                                                PROJ_NAME=project_info.name,
                                                PROJ_UNIQUE_UUID=project_info.proj_unique_uuid)
    
    sln_path = os.path.join(project_info.root_dir, f'{project_info.name}.sln')
    
    file_utils.write_to_file(sln_path, sln_content)

# Create the vcxproj file, which defines:
# - build targets
# - files to show in groups
def create_vcxproj(project_info: run_utils.ProjectInfo):
    vcxproj_path = project_info.proj_dir / f'{project_info.name}.vcxproj'

    src_includes = ""
    for file in project_info.source_files:
        src_includes += constants.CLCOMPLILE_TEMPLATE.format(FILE=file)
    
    hdr_includes = ""
    for file in project_info.header_files:
        hdr_includes += constants.CLINCLUDE_TEMPLATE.format(FILE=file)
    
    res_includes = ""
    for file in project_info.resource_files:
        res_includes += constants.TEXT_TEMPLATE.format(FILE=file)

    vcxproj_content = constants.VCXPROJ_TEMPLATE.format(PROJ_UNIQUE_ID=project_info.proj_unique_uuid,
                                                        PROJ_NAME=project_info.name,
                                                        C_INCLUDES=src_includes,
                                                        H_INCLUDES=hdr_includes,
                                                        RES_INCLUDES=res_includes)
        
    file_utils.write_to_file(vcxproj_path, vcxproj_content)

# Create the vcxproj.vcxfilters file, which defines:
# - filters for which types of files go in the different categories
# - explicity stating which items in the item groups go in the categories
def create_vcxfilters(project_info: run_utils.ProjectInfo):
    vcxproj_filters_path = project_info.proj_dir / f'{project_info.name}.vcxproj.filters'

    src_includes = ""
    for file in project_info.source_files:
        src_includes += constants.FILTER_SOURCE_TEMPLATE.format(FILE=file.parts[-1])
    
    hdr_includes = ""
    for file in project_info.header_files:
        hdr_includes += constants.FILTER_HEADER_TEMPLATE.format(FILE=file.parts[-1])
    
    res_includes = ""
    for file in project_info.resource_files:
        res_includes += constants.FILTER_RESOURCE_TEMPLATE.format(FILE=file.parts[-1])

    vcxproj_filters_content = constants.VCXPROJ_FILTERS_TEMPLATE.format(SOURCE_INCLUDES=src_includes,
                                                                        HEADER_INCLUDES=hdr_includes,
                                                                        RESOURCE_INCLUDES=res_includes)
        
    file_utils.write_to_file(vcxproj_filters_path, vcxproj_filters_content)

# Main Create function to tie all 3 parts together
def create_visual_studio_project(project_info: run_utils.ProjectInfo):
    # Create the .sln file
    create_sln(project_info)

    # Create the .vcxproj file
    create_vcxproj(project_info)

    # Create the .vcxproj.filters file
    create_vcxfilters(project_info)

# Remove vcx files
# for operation `down`
def remove_vcx_files(project_info: run_utils.ProjectInfo):
    # sln
    file_utils.remove_file(os.path.join(project_info.root_dir, f'{project_info.name}.sln'))
    project_info.resource_files.remove(Path(f'{project_info.name}.sln'))

    # vcxproj
    file_utils.remove_file(project_info.proj_dir / f'{project_info.name}.vcxproj')
    project_info.resource_files.remove(Path(project_info.name) / f'{project_info.name}.vcxproj')

    # vcxproj.filters
    file_utils.remove_file(project_info.proj_dir / f'{project_info.name}.vcxproj.filters')
    project_info.resource_files.remove(Path(project_info.name) / f'{project_info.name}.vcxproj.filters')

    # vcxproj.user
    file_utils.remove_file(project_info.proj_dir / f'{project_info.name}.vcxproj.user')
    project_info.resource_files.remove(Path(project_info.name) / f'{project_info.name}.vcxproj.user')

    # update files, not including vcx files now
    project_info.update_all_files()
