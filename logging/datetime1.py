#!/usr/bin/env python3
'''for more control over the formating of the date/time, provide datefmt arg
to basicConfig 
example
'''
import logging
logging.basicConfig(format='%(asctime)s %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when the event was logged.')
