import sys

from argparse import ArgumentParser

from lib.file_processer import FileContentCountPatternFinder

class Options:
    def __init__(self):
        self.filepaths = []
        self.pattern = ''
        self.functions = {'count' : 0, 'sum' : 1, 'display': 2}
        self._init_func_dictionary()
        self._init_parser()
    
    def _init_func_dictionary(self):
        self.finders = { 0:FileContentCountPatternFinder}
        
    def _init_parser(self):
        #overrides usage that is by default something like:
        # usage: PROG [-h] [--foo] [FOO]] bar [bar ...]
        # usage = './bin/run_project'
        self.parser = ArgumentParser() #usage=usage
        # inits the argparser with an argument example with
        # a default value 'example-value'
        # nargs='+' takes 1 or more arguments, nargs='*' takes zero or more.
        self.parser.add_argument('-p',
                                 '--list',
                                 help='example.log',
                                 nargs='+',
                                 required=True
                                 )
        self.parser.add_argument('-re',
                                 '--regex',
                                 dest='regex',
                                 help='An example regex option'
                                 )                                 
        self.parser.add_argument('-f',
                                 '--function',
                                 default=0,
                                 dest='function',
                                 help='count = 0, sum = 1, display = 2',
                                 type = int,
                                 choices=[0, 1, 2]
                                 )
    
    def parse(self, args=None):

        #show parsed in args
        print('Arguments to be used:')
        for _, value in self.parser.parse_args()._get_kwargs():
            if value is not None:
                print(value)
        
        args = self.parser.parse_args()

        self.filepaths = list(args.list)
        self.pattern = args.regex
        function = args.function

        return self.finders[0]