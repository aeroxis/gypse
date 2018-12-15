import click
import logging
import os

from gypse.constants import DEFAULT_CONFIG_HOME, REGEX_URL, REGEX_PHONE, REGEX_EMAIL
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
@click.option('-e', '--extractor', multiple=True, type=click.Choice(['email', 'phone', 'url']), help="email - extracts email; phone - extracts phone numbers; url - extracts urls")
def extract(path, margins, extractor):
    """
    Extracts details from a directory or files based on the extractors you request: email, phone or url.
    """
    logger.debug("Margins will be set to: %d" % margins)
    logger.debug("Extractors specified in call: %s" % str(extractor))

    logger.info("Analyzing Files...")

    # scan the files in the given path 
    line_extractor = LineExtractor(path)
    extracted_lines = line_extractor.extract()

    # extract URLs from each line
    for e in extractor:
        
        if e == 'url':
            resource_type = 'URL'
            resource_regex = REGEX_URL
        elif e == 'phone':
            resource_type = 'Phone Number'
            resource_regex = REGEX_PHONE
        elif e == 'email':
            resource_type = 'E-Mail'
            resource_regex = REGEX_EMAIL
        

        resource_extractor = ResourceExtractor(extracted_lines, resource_regex)
        results = resource_extractor.extract()

        # present report
        printer = ResultsPrinter(resource_type, results)
        printer.print(margins=margins)