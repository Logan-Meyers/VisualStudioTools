import project_classes.solution as SLN_CLASS
from pathlib import PurePath

def main():
    sln = SLN_CLASS.Solution()

    sln.loadSolutionFile(PurePath("/home/nixUser/Downloads/PA7/PA7.sln"))

    print(sln)

main()
