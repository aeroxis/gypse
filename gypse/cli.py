import click
import logging
import os

from gypse.constants import DEFAULT_CONFIG_HOME, REGEX_URL
from gypse.extractor import LineExtractor, ResourceExtractor
from gypse.logging import configureLogger, getLogger
from gypse.printer import ResultsPrinter

logger = getLogger()

@click.group()
@click.option('--debug/--no-debug', help="Prints additional details when Gypse does it's work, so you can see what's going on under the hood.")
def gypse(debug):

    if debug:
        configureLogger("DEBUG")

        logger.debug("Running Gypse in DEBUG mode.")
    else:
        configureLogger("INFO")
        
    logger.info("Starting Gypse...")

@gypse.command()
@click.argument('path')
@click.option('-m', '--margins', default=2, help="Margins allow you to see more or less from the line that was found.")
@click.option('-e', '--extractor', multiple=True, type=click.Choice(['email', 'phone', 'url']))
def extract(path, margins, extractor):

    logger.debug("Margins will be set to: %d" % margins)
    logger.debug("Extractors specified in call: %s" % str(extractor))

    logger.info("Analyzing Files...")

    # scan the files in the given path 
    line_extractor = LineExtractor(path)
    extracted_lines = line_extractor.extract()

    # extract URLs from each line
    if 'url' in extractor:
        resource_type = "URL"
        resource_extractor = ResourceExtractor(extracted_lines, REGEX_URL)
        results = resource_extractor.extract()

        # present report
        printer = ResultsPrinter(resource_type, results)
        printer.print(margins=margins)