# Si7005.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mar 2014 python port of Si7005 arduino library
# AKA

import Si7005
import time

s = Si7005.si7005(pin='P9_21')
# s = Si7005.si7005()
while(1):
	if s.detectSensor():
		print s.getTemperature()
		print s.getHumidity()
else:
	print 'cannot find sensor'
	print s
	time.sleep(1)
