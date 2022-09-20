# module =  A file containing python code. May contain functions, classes, etc. Used with modular programming,
#           which is a concept to separate a program into parts.

#import Submodule as msg             # Imports the entire module 'Submodule' as 'msg', note you cannot import modules
                                    # starting with numbers.

from p37_Module_submodule import hello, bye     # Imports the specified commands from 'Submodule'. '*' can be used to import all.

#msg.hello()                         # Using fucntions from imported module.
#msg.bye()

hello()                             # functions can be used directly w/o a module name if we use the 'from' method to import.
bye()

help("modules")                     # Shows all the pre-written modules that can be imported.
# https://docs.python.org/3/py-modindex.html list of modules.