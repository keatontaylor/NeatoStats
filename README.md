NeatoStats
==========

A collection of python scripts to retrieve statistics on XV Series NeatoRobotics vacuums.

powerStats.py
=============

Displays power consumption, draw, and runtime of your Neato vacuum. 

Required Software:

PySerial - https://pypi.python.org/pypi/pyserial

Testing Procedure:
------------------

To gather power usage data you'll need to isolate the Neato from its charging base. Ideally, you want to place the Neato in a room or area where it will run out 
of power before finishing its cleaning cycle. Next you'll need to connect the Neato via USB to the computer and run this software. See below for the expected output.

If you'd also like to get charging statistics place the Neato on its charging base and let it charge completely. Then reconnect to USB and run this software again. 
You should see a log entry with a negative min current and a low max current in the log along with the associated mAh used and average current showing charging values.

Example Output:


| Log Entry | Runtime/Charge (minutes) | mAh Used / Consumed (mAh) | Min Current (mA) | Max Current (mA) | Average Current (mA) | 
| :-------- | :----------------------- | :------------------------ | :--------------- | :--------------- | :------------------- |
| 376       | 135                      | 51240955760161            | -2095            | 4089             | 5.41706870868e+11    |
| 389       | 28                       | 709                       | 140              | 3211             | 2987                 |



