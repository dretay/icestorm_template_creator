## An simple project to generate a template Icestorm project ##

### Overview ###

Simply invoke the script with something like this:
`python ./icestorm_template_creator/main.py -o and_cont_assign`
and a folder called "and_cont_assign" will be created in your working directory with a populated Makefile and skelleton files

### Main Features ###

- `make sim`
-- synthesizes the circuit and loads it into GTKWave
- `make view`
-- loads the logical schematic into Dot Viewer
- `make sint`
-- builds the bin for uploading 
- `make clean`
-- cleans the project
