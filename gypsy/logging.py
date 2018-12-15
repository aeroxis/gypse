import coloredlogs
import logging

from gypsy.constants import DEFAULT_LOGGER_NAME

def configureLogger(level):

    coloredlogs.install(level=level)
    return logging.getLogger()

def getLogger():

    return logging.getLogger(DEFAULT_LOGGER_NAME)