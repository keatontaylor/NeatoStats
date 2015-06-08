NeatoStats
==========

A collection of python scripts to retrieve statistics on XV Series NeatoRobotics vacuums.

powerStats.py
=============

Displays power consumption, draw, and runtime. Extremely useful when attempting to track down issues with batteries.

Required Software:

PySerial - https://pypi.python.org/pypi/pyserial

Usage:

python powerStats.py

Example Output:

+---------------------------------------------------------+

| Log Entry | Runtime (minutes) | mAh Used | Current Draw | 

+---------------------------------------------------------+

| 376       | 35                | 1988     | 1124         |

| 389       | 28                | 1495     | 709          |

+---------------------------------------------------------+
