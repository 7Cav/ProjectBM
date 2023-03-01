



!pip install pandas as pd
!pip install numpy as np
!pip install datetime
!pip install os
!pip install requests

import datetime
import os
import requests


# Function that returns a list of yyyMM partitions that are needed to update tables
# in a rolling period set by daysAgo
# for example, to update the last 5 days of data (daysAgo=5)

def get_dtParts(daysAgo):
    
    dtPart = []

    startDay = datetime.datetime.now() - datetime.timedelta(days=daysAgo)
    endDay = datetime.datetime.now() - datetime.timedelta(days=1)

    #creates a list of days between the startDay and endDay
    date_list = [startDay + datetime.timedelta(days=x) for x in range(daysAgo)]

    #for each date found in date_list, figures out what the yyyyMM format is, and creates a unique list

    for dt in date_list:
        yyyyMM = int(str(dt)[0:4]+str(dt)[5:7])
        if yyyyMM not in dtPart:
            dtPart.append(yyyyMM)

    return dtPart


def get_etzDates(daysAgo):

    startDay = datetime.datetime.now() - datetime.timedelta(days=daysAgo)
    endDay = datetime.datetime.now() - datetime.timedelta(days=1)

    #creates a list of days between the startDay and endDay
    date_list = []
    for x in range(daysAgo):
        dt = (startDay + datetime.timedelta(days=x)).date()
        date_list.append(dt)
    return date_list


def get_beginAndEnd(daysAgo):
    date_list = []
    startDay = datetime.datetime.now() - datetime.timedelta(days=daysAgo)
    endDay = datetime.datetime.now() - datetime.timedelta(days=1)

    startDay_string = startDay.strftime('%Y-%m-%d')
    endDay_string = endDay.strftime('%Y-%m-%d')

    date_list.append(startDay_string)
    date_list.append(endDay_string)

    return date_list



