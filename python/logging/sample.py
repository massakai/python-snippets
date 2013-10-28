#!/usr/bin/python

import logging
import logging.config

logging.config.fileConfig('log.conf')

logging.debug('This is debug message.')
logging.info('This is info message.')
logging.warning('This is warning message.')
logging.error('This is error message.')
logging.critical('This is critical message.')
