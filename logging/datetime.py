#!/usr/bin/env python3
'''to display the date and time of an event by placing '%(asctime)s' in your
format string
example
'''
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
