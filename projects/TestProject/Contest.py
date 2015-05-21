'''
Refer to design notes at:
https://github.com/Shrinking-World/Impact-SRS/wiki/Marketplace-of-Ideas-Reset
'''

import datetime

__author__ = 'dreiger'

_startDate = ''
_endDate = ''

def setContestDates(startDate, interval):
    # TODO Do date validation
    _startDate = startDate

    # TODO Calculate the end date based on the interval
    _endDate = ''

def setContestDates(startDate, endDate):
    # TODO Do date validation
    _startDate = startDate
    _endDate = endDate

def getStartDate():
    return _startDate

def getEndDate():
    return _endDate

def isContestEnded():
    current = datetime.datetime.now()
    git
    # TODO Determine whether the current date is greater than the contest end date.
    return False

