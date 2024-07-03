#!/usr/bin/env python3
'''to change the format which is used to display messages you need
to specify the format you want to use.
'''
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
logging.critical("and this too i guess")
