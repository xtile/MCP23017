#!/usr/bin/python
'''
Exemple 'How to use the library MCP23017_I2C' - Rui Pedro Silva; Portugal; 03/2015
Connect a switch to GPB7 and led to GPA0. This program will make the LED turn on when you turn the switch.
'''
from MCP23017_I2C import *

GPIO_CHIP_1 = GPIO_CHIP(0x20, 1) # define chip MCP23017_I2C
#   GPIO_CHIP( Device address, Pi Model )
# 0 = Model A, B Rev 2 or B+ Pi ; 1 = Model B Rev 1 Pi) 

GPIO_CHIP_1.setup( 0, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 1, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 2, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 3, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 4, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 5, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 6, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 7, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 0, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 1, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 2, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 3, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 4, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 5, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 6, 'OUT', 'B') # configure GPA0 like output
GPIO_CHIP_1.setup( 7, 'OUT', 'B') # configure GPA0 like output
# GPIO_CHIP.setup(pin, io, side)
# 	pin (0 - 7)  io (IN or OUT)  side (A or B)


# You can use another MCP23017, write:
#GPIO_CHIP_2 = GPIO_CHIP(0x21, 1) # define another chip MCP23017_I2C

#GPIO_CHIP_2.setup( 0, 'OUT', 'A') # configure GPA0 like output
#GPIO_CHIP_2.setup( 7, 'IN', 'B') # configure GPB7 like input

try:
	while 1:
		GPIO_CHIP_1.output(0, 0, 'B') # save the state of GPB7 in 'switch'
		GPIO_CHIP_1.output(1, 0, 'B') # save the state of GPB7 in 'switch'
		print 'zero state'
		sleep 5
		GPIO_CHIP_1.output(0, 1, 'B') # save the state of GPB7 in 'switch'
		GPIO_CHIP_1.output(1, 0, 'B') # save the state of GPB7 in 'switch'
		print 'after 1'
		sleep 5
		GPIO_CHIP_1.output(0, 0, 'B') # save the state of GPB7 in 'switch'
		GPIO_CHIP_1.output(1, 0, 'B') # save the state of GPB7 in 'switch'	
		print 'after 2'
		sleep 5
		GPIO_CHIP_1.output(0, 0, 'B') # save the state of GPB7 in 'switch'
		GPIO_CHIP_1.output(1, 1, 'B') # save the state of GPB7 in 'switch'	
		print 'after 2'
		sleep 5
		# GPIO_CHIP.input(pin, side)		
except KeyboardInterrupt:
	print 'End exemple.py!'
