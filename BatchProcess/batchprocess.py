# Example of a very simple batch processing script

from anypytools import AnyPyProcess

macro = ['load "main.any"',
         'operation Main.Study.Kinematics',
         'run']

app = AnyPyProcess(num_processes = 1)

app.start_macro(macro, search_subdirs= "Trial[0-9]{2}.*main.any" )


