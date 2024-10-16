import os, uuid
from file_utils import *

# Create the updated vcxproj file in the project folder
def create_vcxproj(new_project_dir, source_files, header_files, resource_files, project_name):
    vcxproj_path = os.path.join(new_project_dir, f'{project_name}.vcxproj')

    vcxproj_content = """<Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <ItemGroup>
    """
    
    # Add source files (relative paths)
    for src in source_files:
        relative_src = os.path.basename(src)
        vcxproj_content += f'    <ClCompile Include="{relative_src}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n  <ItemGroup>\n'
    
    # Add header files (relative paths)
    for hdr in header_files:
        relative_hdr = os.path.basename(hdr)
        vcxproj_content += f'    <ClInclude Include="{relative_hdr}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n  <ItemGroup>\n'
    
    # Add resource files (relative paths)
    for res in resource_files:
        relative_res = os.path.basename(res)
        vcxproj_content += f'    <None Include="{relative_res}" />\n'
    
    vcxproj_content += '  </ItemGroup>\n</Project>'
    
    with open(vcxproj_path, 'w') as vcxproj_file:
        vcxproj_file.write(vcxproj_content)

# Create the solution file and point to the new vcxproj location with proper formatting and GUID
def create_sln(project_dir, project_name):
    project_guid = str(uuid.uuid4()).upper()  # Generate a unique GUID for the project

    sln_content = f"""Microsoft Visual Studio Solution File, Format Version 12.00
        # Visual Studio Version 17
        VisualStudioVersion = 17.11.35312.102
        MinimumVisualStudioVersion = 10.0.40219.1
        Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{project_name}", "{project_name}\\{project_name}.vcxproj", "{{{project_guid}}}"
        EndProject
        Global
            GlobalSection(SolutionConfigurationPlatforms) = preSolution
                Debug|x64 = Debug|x64
                Release|x64 = Release|x64
            EndGlobalSection
            GlobalSection(ProjectConfigurationPlatforms) = postSolution
                {{{project_guid}}}.Debug|x64.ActiveCfg = Debug|x64
                {{{project_guid}}}.Debug|x64.Build.0 = Debug|x64
                {{{project_guid}}}.Release|x64.ActiveCfg = Release|x64
                {{{project_guid}}}.Release|x64.Build.0 = Release|x64
            EndGlobalSection
            GlobalSection(SolutionProperties) = preSolution
                HideSolutionNode = FALSE
            EndGlobalSection
        EndGlobal
        """
    
    sln_path = os.path.join(project_dir, f'{project_name}.sln')
    
    with open(sln_path, 'w') as sln_file:
        sln_file.write(sln_content)

# Main function to tie everything together
def create_visual_studio_project(project_dir, project_name):
    source_files, header_files, resource_files = categorize_files(project_dir)

    # Move all files into the new {project_name} folder
    new_project_dir = move_files_to_project_folder(source_files, header_files, resource_files, project_name, project_dir)

    # Create the .vcxproj and .sln files
    create_vcxproj(new_project_dir, source_files, header_files, resource_files, project_name)
    create_sln(project_dir, project_name)