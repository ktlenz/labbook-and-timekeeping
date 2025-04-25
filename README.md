# Labbook and Timekeeping
A python project to document thought processes, coding challenges and other stuff like a lab book which also delineates a proper time table of time spent working.

## Table of Contents
- [Description](#description)
- [To-Do](#to-do)
- [Environment](#environment)
- [License](#license)
- [Contact and Citation](#contact-and-citation)

## Description
I want to start a program by clickling on an app which opens a window. 

I can select whether I want to create a new lab book or open an existing one or save the lab book. Clicking on either button will open the explorer window to select a file. The new lab book will give the opportunity to select a file name and location. The open lab book will open the file explorer to select a file. The save lab book will save the current lab book to the location.

Further, there are multiple buttons from which I can choose to generate a new entry in the lab book. The buttons are:
* Started working
* Finished working
* Thought
* Problem
* Coding
* Research
* Other
Each button press will create a time stamped entry with the option to add a comment.

There is a final button to generate a time table. First, there is a check whether each Started working entry has a corresponding Finished working entry. If not, the user is prompted to add a Finished working entry or insert a preset time (e.g. 30 minutes). Afterwards, the time table is generated to match a predefined format and saved to a file.

## To-Do

1. Add URL to Citation file
1. Create the python environment, install the required packages and export environment to GitHub.
1. 

## Environment
The python [environment](environment.yml) used to solve the exercises is provided as well.

## License
This Project is licensed under the [MIT License](LICENSE).

## Contact and Citation
Feel free to contact me via kilian.lenz[at]uni-potsdam.de.\
If you want to use the provided code, please note the [Citation](CITATION.cff).