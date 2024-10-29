# VisualStudioTools

A simple Python Script that allows you to Convert basic projects to and from Visual Studio Code and Visual Studio 2022.

This is intended to work cross-platform, as such:

- Windows VS Code <-> Windows VS 2022
- Mac VS Code <-> Windows VS 2022
- Linux VS Code <-> Windows VS 2022

So all OS's can convert a VS 2022 Code project from Windows to a VS Code project for editing capabilities, and then back to a VS 2022 project to be ran on Windows.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Program Usage](#program-usage)
- [Example Project Conversion Scenario](#example-project-conversion-scenario)
  - Base file structure
  - Converted file structure
  - VS 2022 file structure
- [Notable Resources]()

## Prerequisites

All you need to run this program is:
- to have downloaded the latest zip of this repository (You may click ([here](https://github.com/TheTerrarian03/VSCode_to_VS/archive/refs/heads/main.zip)) to auto-download from github)
- and at least Python 3.12 (earlier may work, but older versions are untested). You may find Python here ([https://www.python.org/downloads/](https://www.python.org/downloads/)) or installed via [homebrew](https://brew.sh/) or in the Microsoft Store.

## Program Usage

Currently there is only two ways to use the program:
- `python .\main.py [your project folder path here]` to convert a project. Example usage: [`python .\main.py 'c:\Users\You\Desktop\ImportantProject\`]
- `python .\main.py [project folder path here] [project type]` where `[project type]` is either:
  - `C++`
  - `C#`

## Example Project Conversion Scenario

Base file structure for C program:
- [Project Name]
  - `main.c` - main program, includes "utils.h"
  - `utils.c` - defines functions for "utils.h"
  - `utils.h` - function headers and includes for main and "utils.c"
  - `inputs.dat` - some input file to read from
  - `output.txt` - some output file to write to

Converted file structure for VS 2022
- [Project Name]
  - [Project Name]
    - `main.c` - main program, includes "utils.h"
    - `utils.c` - defines functions for "utils.h"
    - `utils.h` - function headers and includes for main and "utils.c"
    - `inputs.dat` - some input file to read from
    - `output.txt` - some output file to write to
    - `[Project Name].vcxproj` - Outlines project configurations and files to include
    - `[Project Name].vcxproj.filters` - Classifies files for Visual Studio to categorize files into, such as "Source Files", "Header Files", and "Resourse Files"
  - `[Project Name].sln` - Solution file for VS 2022 to read

Which then the file structure will look like this in Visual Studio 2022:
- Header Files
  - `utils.h`
- Resource Files
  - `inputs.dat`
  - `output.txt`
- Source Files
  - `main.c`
  - `utils.c`

## Notable Resources

Below is a link to Visual Studio project GUIDS, for both myself's future reference, and your curiosity:
https://stackoverflow.com/questions/10802198/visual-studio-project-type-guids

Also below is a link to my colleague's version of my project, go check it out!!
https://github.com/Huskiefusion/vs-sln-gen
(Note: This repo may be private)