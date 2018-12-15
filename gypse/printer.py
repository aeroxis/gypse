import click
import os

from gypse.base import Base

class ResultsPrinter(Base):

    def __init__(self, resource_type, results):
        
        super(ResultsPrinter, self).__init__()
        self.resource_type = resource_type
        self.results = results

    def print(self, margins=2):

        self.logger.info("Presenting Results...")
        rows, columns = os.popen('stty size', 'r').read().split()
        main_head_line = '-' * int(columns)
        sub_head_line = '+' * (int(columns) - 4)
        for resource, details in self.results.items():
            
            header = "%s: %s" % (self.resource_type, resource)

            click.secho(main_head_line, fg='green', bold=True)
            click.secho(header, fg='green', bold=True)
            click.secho(main_head_line, fg='green', bold=True)
            
            header_printed = False
            for detail in details:

                path_to_file, line_no, line = detail
                printer = LinePrinter(path_to_file, line_no, margins)
                if not header_printed:
                    printer.print_header()
                    header_printed = True
                else:
                    printer.print_separator()
                printer.print()

class LinePrinter(Base):

    def __init__(self, path_to_file, line_no, margins):

        super(LinePrinter, self).__init__()
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
            