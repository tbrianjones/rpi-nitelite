import RPIO.PWM as PWM
import time as time

PWM.setup()
PWM.init_channel( 0, 10000 )
PWM.print_channel( 0 )

while True:

	# open pulse width file for reading
	f = open( 'pulse_widths', 'r' )
	red_pw		= int( f.readline().rstrip( '\n' ) )
	green_pw	= int( f.readline().rstrip( '\n' ) )
	blue_pw		= int( f.readline().rstrip( '\n' ) )
	white_pw	= int( f.readline() )
	
	# red
	if red_pw == 0:
		PWM.clear_channel_gpio( 0, 23 )
	else:
		PWM.add_channel_pulse( 0, 23, 0, red_pw )

	# green
	if green_pw == 0:
		PWM.clear_channel_gpio( 0, 24 )
	else:
		PWM.add_channel_pulse( 0, 24, 0, green_pw )

	# blue
	if blue_pw == 0:
		PWM.clear_channel_gpio( 0, 25 )
	else:
		PWM.add_channel_pulse( 0, 25, 0, blue_pw )
	
	# white
	if white_pw == 0:
		PWM.clear_channel_gpio( 0, 22 )
	else:
		PWM.add_channel_pulse( 0, 22, 0, white_pw )
	
	
	time.sleep( 0.5 )