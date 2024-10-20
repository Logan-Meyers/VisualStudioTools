import vcx_utils, file_utils, run_utils, os, pathlib, constants

# main function
def main():
    if not run_utils.are_arguments_valid():
        print("\nSorry! Incorrect usage of the tool. Please see the usage instructions below:\n\npython main.py [root project directory] [project type (optional, defaults to C++)]")
        quit()

    # create and generate project information
    proj_info = run_utils.project_info()
    proj_info.generate_main_info(run_utils.get_project_dir_arg(), run_utils.get_project_type_arg())
    proj_info.generate_file_info()

    # print info about the project
    proj_info.display_info()

    # convert the project
    # move the necessary files, creating directories as needed
    file_utils.move_files_to_project_folder(proj_info)

    # create the various files for Visual Studio
    vcx_utils.create_visual_studio_project(proj_info)

    # print(vcx_utils.create_vcxfilters(proj_info))

main()
