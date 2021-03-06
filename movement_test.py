#!/usr/bin/env python
"""Move Rectangle Farmware"""
#Import libraries
from farmware_tools import device
from farmware_tools import get_config_value

#Define functions
def moveAbs(x, y, z):
    device.log('Moving to ' + str(x) + ', ' + str(y) + ', ' + str(z), 'success', ['toast'])
    device.move_absolute(
        {
            'kind': 'coordinate',
            'args': {'x': x, 'y': y, 'z': z}
        },
        100,
        {
            'kind': 'coordinate',
            'args': {'x': 0, 'y': 0, 'z': 0}
        }
    )

#Call functions
moveAbs(600, 150, -200) 

device.log('success!!', 'success', ['toast'])

if __name__ == '__main__':
    farmware_name = 'move_to_safe'
