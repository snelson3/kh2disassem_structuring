This repo contains two files to help with understanding the 2.5 KH2FM debug disassembly

It requires the disassembled source file `BLJM_66675.c` to be put in this folder

### structure_dissassem.py

Running this file will split out the single source file into a directory tree, to make for easier perusing. It does a really simple structure, IE this function

`YS::SUMMON_TABLE::read(const YS::SUMMON_TABLE *const this)`

Will create the following inside a "source" root folder

YS
  SUMMON_TABLE
    read.cpp

Where YS and SUMMON_TABLE are folders and read.cpp is a file containing only the functions with that name

After running there are also two files put in the "source" root

`function_declarations` - contains a list of the function names in the order given by the disassembled file. Important for going backwards from the directory structure into a single file

`data_declarations` - definition of a bunch of variables used by different functions

Eventually it will be able to go backwards.

### gen_source_tree.py 

`source_tree.txt` contains the most well known list of what the development KH2 source code tree looks like. `gen_source_tree.py` creates a dummy file tree according to this file. I made this because I find it easier on the eyes to read the file tree in VSCode, as opposed to a text list of file paths.