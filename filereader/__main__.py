import sys
import argparse

from lib import Project
from lib import Options


# from lib import filecontentfinder

def run_project(args):
    options = Options()
    

    function = options.parse(args[1:])
    finder = function(options)
    finder.process_file_contents()


    # project = Project(options)

    # print ('Printing date:', project.date())
    # print ('Printing example arg:', project.print_example_arg())

if __name__ == '__main__':
    run_project(sys.argv)