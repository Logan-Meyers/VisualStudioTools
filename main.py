import vcx_utils, file_utils, run_utils, os

MAIN_UUID = "FAE04EC0-301F-11D3-BF4B-00C04F79EFBC"

# main function
def main():
    if not run_utils.are_arguments_valid():
        print("Sorry! Incorrect usage of the tool. Please see the usage instructions below:\n\npython main.py [root project directory]")
        quit()

    # create and generate project information
    proj_info = run_utils.project_info()
    proj_info.generate_main_info(run_utils.get_project_dir_arg())

    
    print(proj_info.name)

# Example usage
# project_dir = '/Users/lsm03/Desktop/Programming/College/CompSciCode/CPT_S 121/Extra Credit/BlackJackTest'
# project_name = 'BlackJackTest'
# create_visual_studio_project(project_dir, project_name)

main()
