import click
import os

from gypse.base import Base

class LinePrinter(Base):

    def __init__(self, path_to_file, line_no, margins):

        rows, columns = os.popen('stty size', 'r').read().split()
        self.width = int(columns)
        self.path_to_file = path_to_file
        self.line_no = int(line_no)
        self.margins = int(margins)

    def print_header(self):

        subheader = "Contents of %s" % self.path_to_file
        subheader_sep = "-" * len(subheader)
        click.secho("    %s" % subheader_sep, fg='magenta', bold=True)
        click.secho("    %s" % subheader, fg='magenta', bold=True)
        click.secho("    %s" % subheader_sep, fg='magenta', bold=True)

    def print_separator(self):

        click.secho("    | ... | .........................................................", fg='magenta', bold=True)

    def print(self):

        with open(self.path_to_file) as f:

            lines = f.readlines()
            start = self.line_no - self.margins
            end = self.line_no + self.margins + 1
            total_lines = self.margins + 1 + self.margins

            if total_lines > len(lines):
                start = 0
                end = len(lines)


            for i, line in enumerate(lines[start : end]):
                line_no = start + i
                bold = (line_no == self.line_no)
                click.secho("    | %s | %s" % (start + i, line.strip('\n')), fg='magenta', bold=bold)
            