#!/usr/bin/env python
'''

Copyright (C) 2015 Keaton S. Taylor http://keatonstaylor.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Revision History:

June 7th, 2015 Keaton Taylor	Initial Release. 

'''

import csv
import serial
import StringIO

#SERIAL_PORT = '/dev/tty'		# Linux
SERIAL_PORT = '/dev/tty.usbmodem1451'	# Mac/Unix

try:
    robot = serial.Serial(SERIAL_PORT, 115200, \
        serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE,  1.0)
except:
    print('Unable to connect to Neato on serial port ' + SERIAL_PORT )
    exit()

robot.write('GetLifeStatLog\n') 

foundRun = False

print '+-------------------------------------------------------------------------------------------------------------------------------+'
print '| Log Entry | Runtime/Charge (minutes) | mAh Used / Consumed (mAh) | Min Current (mA) | Max Current (mA) | Average Current (mA) |' 
print '+-------------------------------------------------------------------------------------------------------------------------------+'

while True:
    line = robot.readline()
    if line == chr(26):
        break
    for row in csv.reader(StringIO.StringIO(line)):
        if len(row) == 7:
            if row[1] == 'LS_RunDate':
                foundRun = True
            if foundRun == True:
                if row[1] == 'LS_A2D13':
                    totalCurrent = int(row[5], 0)
                    runTime =  int(row[2])
                    minCur = int(row[3])
                    maxCur = int(row[4])
                    print '| ' + str(row[0]).ljust(10) + '| ' + str(runTime/6000).ljust(25) + '| ' \
                        + str(totalCurrent/360000).ljust(26) + '| ' + str(minCur).ljust(17) + '| ' + str(maxCur).ljust(17) + '| ' + str(totalCurrent/runTime).ljust(21) + '|'
                    foundRun = False

print '+-------------------------------------------------------------------------------------------------------------------------------+'
print '| Rows with negitive min current values include charge cycles and cause incorrect mAh Used / Consumed, run / charge time, and   |'  
print '| average current readings. Please see the README for more information on testing procedures.                                   |'
print '+-------------------------------------------------------------------------------------------------------------------------------+'
robot.close()
