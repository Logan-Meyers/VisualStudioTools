import project_classes.solution as SLN_CLASS
from pathlib import PurePath

def main():
    sln = SLN_CLASS.Solution()

    sln.loadSolutionFile(PurePath("/home/nixUser/Downloads/PA7/PA7.sln"))
    # sln.loadSolutionFile(PurePath("/home/nixUser/Downloads/CPTS_122_SP25-main/Lab_Solutions/Lab_Solutions.sln"))

    print(sln)

main()
