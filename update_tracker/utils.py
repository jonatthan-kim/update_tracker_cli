from enum import IntEnum
from collections import namedtuple
from datetime import datetime
from dateutil import tz

class Level(IntEnum):
    MAJOR = 1
    MINOR = 2
    PATCH = 3

PackageData = namedtuple(
    'PackageData', [
        'current_version', 'updated_version', 'upload_time'
        ]
    )

# Print iterations progress
# reference: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console 
def printProgressBar (iteration, total, prefix = 'Progress:', suffix = '', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

# https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local-datetime 참조
def from_utc_to_local(utc_time):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc_datetime_object = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')
    utc_datetime_object = utc_datetime_object.replace(tzinfo=from_zone)
    return utc_datetime_object.astimezone(to_zone).strftime('%Y-%m-%d %H:%M:%S')
