import vcx_utils, file_utils, run_utils
import constants

# main function
def main():
    if not run_utils.are_arguments_valid():
        print("\nSorry! Incorrect usage of the tool. Please see the usage below:")
        run_utils.print_usage()

    run_args = run_utils.make_run_args()

    print(run_args.conversion_type)
    print(run_args.project_path)
    print(run_args.args)

    # at this point are_arguments_valid MUST be true.

    # create and generate project information
    proj_info = run_utils.ProjectInfo()
    proj_info.generate_main_info(run_args.project_path, run_utils.get_project_type_arg(run_args.args))
    proj_info.generate_file_info()

    # print info about the project
    proj_info.display_info()

    # convert the project
    if run_args.conversion_type == "up":
        # remove unnecessary files if told to
        if "--remove-unnecessary" in run_args.args:
            print("Removing unnecessary files...")
            file_utils.remove_unnecessary_files(proj_info)

        print("Resource files: {}".format(proj_info.resource_files))

        # # move the necessary files, creating directories as needed
        file_utils.move_files_to_project_folder(proj_info)

        # # create the various files for Visual Studio
        vcx_utils.create_visual_studio_project(proj_info)
    elif run_args.conversion_type == "down":
        # do thing
        pass
    elif run_args.conversion_type == "sync":
        # do thing
        pass

# run the main function
main()
