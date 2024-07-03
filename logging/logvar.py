#!/usr/bin/env python3
'''to log variable data, use a format string for the event desc message
and a[ppend the var data as args.
for example:
'''
import logging
logging.warning('%s before you %s', 'look', 'leap!')

#expected output
#WARNING:root:look before you leap!
