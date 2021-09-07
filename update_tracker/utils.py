from enum import IntEnum
from collections import namedtuple

class Level(IntEnum):
    MAJOR = 1
    MINOR = 2
    MICRO = 3

PackageData = namedtuple(
    'PackageData', [
        'current_version', 'updated_version', 'upload_time'
        ]
    )