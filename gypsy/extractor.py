import os
import re

from gypsy.base import Base
from gypsy.constants import REGEX_URL
from gypsy.data.url import URL

class LineExtractor(Base):
    '''
    Scans a path that's provided and scans for lines from the contents of 
    the directory or file represented by that path.
    '''
    def __init__(self, path):

        super(LineExtractor, self).__init__()
        self.path = path
        self.is_dir = os.path.isdir(path)

    def extract_lines_from_file(self, path_to_file):

        extracted = {}
        lines = []

        # pull out the lines from the file
        with open(path_to_file) as f:
            lines = f.readlines()

        # put the lines in a nicely formatted dictionary
        if path_to_file not in extracted:
            extracted[path_to_file] = {}

        for i, line in enumerate(lines):
            extracted[path_to_file][i] = line
        
        return extracted


    def extract(self):
        '''
        Extracts lines out of files.
        '''
        extracted = {}

        if self.is_dir:
            for root, dirs, files in os.walk(self.path, topdown=True):

                for name in files:

                    path_to_file = os.path.join(root, name)
                    self.logger.debug("Scanning '%s'" % path_to_file)

                    # read the file and extract the lines out of the files
                    extracted_data = self.extract_lines_from_file(path_to_file)
                    extracted.update(extracted_data)
        else:
            extracted_data = self.extract_lines_from_file(self.path)
            extracted.update(extracted_data)

        return extracted

class URLExtractor(Base):

    def __init__(self, lines_extracted):
        super(URLExtractor, self).__init__()
        self.regex = re.compile(REGEX_URL, flags=re.IGNORECASE)
        self.lines_extracted = lines_extracted

    def extract_url(self, line):
        '''
        Extracts URL from a line if it exists.
        '''
        results = self.regex.findall(line)
        if results:
            self.logger.debug("Line '%s' has '%s'" % (line, results))
        return results


    def extract(self):

        results = {}

        for path_to_file, content in self.lines_extracted.items():
            for line_number, line in content.items():
                
                urls_in_line = self.extract_url(line)
                for u in urls_in_line:

                    # u = URL(u)
                    if u in results:
                        results[u].append(
                            (path_to_file, line_number, line)
                        )
                    else:
                        results[u] = [
                            (path_to_file, line_number, line)
                        ]
        return results