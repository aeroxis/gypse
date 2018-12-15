import click
import logging
import os

from gypsy.constants import DEFAULT_CONFIG_HOME
from gypsy.extractor import LineExtractor, URLExtractor
from gypsy.logging import configureLogger, getLogger
from gypsy.printer import LinePrinter

logger = getLogger()

@click.group()
@click.option('--debug/--no-debug')
def gypsy(debug):

    if debug:
        configureLogger("DEBUG")

        logger.debug("Running Gypsy in DEBUG mode.")
    else:
        configureLogger("INFO")
        
    logger.info("Starting Gypsy...")

# @gypsy.command()
# def setup():
#     """
#     Sets up Gypsy on your machine.
#     """
#     logger.info("Setting up Gypsy")

#     # create default config home
#     if not os.path.exists(DEFAULT_CONFIG_HOME):
#         logger.info("Created directory '%s'" % DEFAULT_CONFIG_HOME)
#         os.makedirs(DEFAULT_CONFIG_HOME)

@gypsy.command()
@click.argument('path')
@click.option('-m', '--margins', default=2, help="Margins allow you to see more or less from the line that was found.")
def url_extractor(path, margins):

    logger.info("Analyzing Files...")
    rows, columns = os.popen('stty size', 'r').read().split()

    # scan the files in the given path 
    line_extractor = LineExtractor(path)
    extracted_lines = line_extractor.extract()

    # extract URLs from each line
    url_extractor = URLExtractor(extracted_lines)
    extracted_urls = url_extractor.extract()

    # present report
    logger.info("Presenting Results...")
    main_head_line = '-' * int(columns)
    sub_head_line = '+' * (int(columns) - 4)
    for url, details in extracted_urls.items():

        header = "URL: %s" % url

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

        # for detail in details:
        #     path_to_file, line_no, line = detail
            
        #     click.secho("    Path:    %s" % path_to_file, fg='magenta')
        #     click.secho("    Line No: %s" % line_no, fg='magenta')
        #     click.secho("    Line:    %s" % line, fg='magenta')
        #     click.secho("    %s" % sub_head_line, fg='magenta')

