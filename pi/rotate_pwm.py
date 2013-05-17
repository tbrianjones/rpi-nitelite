import RPIO.PWM as PWM
import time as time
from random import randint

PWM.setup()
PWM.init_channel( 0, 10000 )
PWM.print_channel( 0 )

r = 10
g = 10
b = 10

r_sign = 1
g_sign = 1
b_sign = 1

while True:
	
	# red
	if r == 10 and not r_sign:
		r_sign = 1
	elif r == 490 and r_sign:
		r_sign = 0
	else:
		PWM.add_channel_pulse( 0, 23, 0, r )
		if r_sign:
			r = r + 10
		else:
			r = r - 10
	
	# green
	if g == 10 and not g_sign:
		g_sign = 1
	elif g == 180 and g_sign:
		g_sign = 0
	else:
		PWM.add_channel_pulse( 0, 24, 0, g )
		if g_sign:
			g = g + 5
		else:
			g = g - 5
	
	# blue
	if b == 10 and not b_sign:
		b_sign = 1
	elif b == 300 and b_sign:
		b_sign = 0
	else:
		PWM.add_channel_pulse( 0, 25, 0, b )
		if b_sign:
			b = b + 5
		else:
			b = b - 5
	
	time.sleep( 0.1 )