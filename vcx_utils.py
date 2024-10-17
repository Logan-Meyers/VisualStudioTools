import os, uuid, file_utils, run_utils

# Create the solution file, including basic information like:
# - Visual Studio version
# - Project name
# - vcxproj location
# - UUIDs
# - build options
def create_sln(project_info: run_utils.project_info):
    sln_content = f"""Microsoft Visual Studio Solution File, Format Version 12.00
        # Visual Studio Version 17
        VisualStudioVersion = 17.11.35312.102
        MinimumVisualStudioVersion = 10.0.40219.1
        Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{project_info.name}", "{project_info.name}\\{project_info.name}.vcxproj", "{{{project_info.project_uuid}}}"
        EndProject
        Global
            GlobalSection(SolutionConfigurationPlatforms) = preSolution
                Debug|x64 = Debug|x64
                Release|x64 = Release|x64
            EndGlobalSection
            GlobalSection(ProjectConfigurationPlatforms) = postSolution
                {{{project_info.project_uuid}}}.Debug|x64.ActiveCfg = Debug|x64
                {{{project_info.project_uuid}}}.Debug|x64.Build.0 = Debug|x64
                {{{project_info.project_uuid}}}.Release|x64.ActiveCfg = Release|x64
                {{{project_info.project_uuid}}}.Release|x64.Build.0 = Release|x64
            EndGlobalSection
            GlobalSection(SolutionProperties) = preSolution
                HideSolutionNode = FALSE
            EndGlobalSection
        EndGlobal
        """
    
    sln_path = os.path.join(project_info.dir, f'{project_info.name}.sln')
    
    file_utils.write_to_file(sln_path, sln_content)

# Create the vcxproj file, which defines:
# - build targets
# - files to show in groups
def create_vcxproj(project_info: run_utils.project_info):
    vcxproj_path = os.path.join(project_info.dir, f'{project_info.name}.vcxproj')

    vcxproj_content = """<?xml version="1.0" encoding="utf-8"?>
    <Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup>
    """
    
    # Add header files (relative paths)
    for hdr in project_info.header_files:
        relative_hdr = os.path.basename(hdr)
        vcxproj_content += f'    <ClInclude Include="{relative_hdr}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n  <ItemGroup>\n'

    # Add resource files (relative paths)
    for res in project_info.header_files:
        relative_res = os.path.basename(res)
        vcxproj_content += f'    <None Include="{relative_res}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n</Project>'

    # Add source files (relative paths)
    for src in project_info.source_files:
        relative_src = os.path.basename(src)
        vcxproj_content += f'    <ClCompile Include="{relative_src}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n  <ItemGroup>\n'
    
    file_utils.write_to_file(vcxproj_path, vcxproj_content)

# Create the vcxproj.vcxfilters file, which defines:
# - filters for which types of files go in the different categories
# - explicity stating which items in the item groups go in the categories
def create_vcxfilters(project_info: run_utils.project_info):
    pass

# Main function to tie everything together
def create_visual_studio_project(project_info: run_utils.project_info):
    # Move all files into the new {project_name} folder
    new_project_dir = file_utils.move_files_to_project_folder(project_info)

    # Create the .vcxproj and .sln files
    create_vcxproj(new_project_dir, source_files, header_files, resource_files, project_name)
    create_sln(project_dir, project_name)