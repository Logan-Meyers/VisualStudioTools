import vcx_utils, file_utils, run_utils, os

# main function
def main():
    if not run_utils.are_arguments_valid():
        print("\nSorry! Incorrect usage of the tool. Please see the usage instructions below:\n\npython main.py [root project directory] [project type (optional, defaults to C++)]")
        quit()

    # create and generate project information
    proj_info = run_utils.project_info()
    proj_info.generate_main_info(run_utils.get_project_dir_arg(), run_utils.get_project_type_arg())
    proj_info.generate_file_info()

    # debugging
    proj_info.display_info()

# Example usage
# project_dir = '/Users/lsm03/Desktop/Programming/College/CompSciCode/CPT_S 121/Extra Credit/BlackJackTest'
# project_name = 'BlackJackTest'
# create_visual_studio_project(project_dir, project_name)

main()
