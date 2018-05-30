import os
import sys
import re
import codecs

from lib.process import Process

class FileContentCountPatternFinder:

    def __init__(self, options):
        self.options = options
        self.process = Process()
        #self.filepaths = options.filepaths #[] 
        #self.find_pattern = options.pattern #sys.argv[5]
        self.regex = re.compile(options.pattern)
        #self.function = options.function

    def process_file_contents(self):
        
        if len(self.options.filepaths) <= 0:
            print(f"Files are required.")
            sys.exit()

        result_list = []
        for filepath in self.options.filepaths:

            if not os.path.isfile(filepath):
                print(f"File {filepath} does not exist.")
                sys.exit()

            count = 0
            with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    matched = self.regex.match(line.strip())
                    if matched:
                        count += int(matched.groups()[1])
                        print(f"Count: {count}")
            result_list.append((filepath, count))
        
        
        results = tuple(result_list)
        for filepath,count in results:
            print(f"A total {count} found in {filepath} using regex '{self.options.pattern}'")