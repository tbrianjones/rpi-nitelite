# import required python libraries
import RPIO
import RPIO.PWM as PWM
import time
import random

# gpio pins
red_gpio	= 23
green_gpio	= 24
blue_gpio	= 25
white_gpio	= 22
motion_gpio	= 18

# settings
motion_delay				= 0		# motion delay trigger ( boolean, 0 or 1 )
motion_delay_cycles			= 1200	# cycles, time dependent on sleep functions
num_motion_delay_cycles 	= 0		# number of cycles since last motion detected

# initiate motion input pin
RPIO.setup( motion_gpio, RPIO.IN )

# initiate software PWM
PWM.setup()
PWM.init_channel( 0, 10000 )
PWM.print_channel( 0 )

# start infinite loop
first_cycle = 1
while True:
	
	# first cycle
	#
	#	- fun startup lighting sequence
	#	- then turns all pins on in case some of the config_colors are set to zero
	#
	if first_cycle == 1:
		PWM.add_channel_pulse( 0, red_gpio, 0, 200 )
		time.sleep( 0.6 )
		PWM.clear_channel_gpio( 0, red_gpio )
		PWM.add_channel_pulse( 0, green_gpio, 0, 100 )
		time.sleep( 0.6 )
		PWM.clear_channel_gpio( 0, green_gpio )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 100 )
		time.sleep( 0.6 )
		PWM.clear_channel_gpio( 0, blue_gpio )
		PWM.add_channel_pulse( 0, white_gpio, 0, 100 )
		time.sleep( 0.6 )
		PWM.clear_channel_gpio( 0, white_gpio )
		time.sleep( 0.6 )
		first_cycle = 0
		continue
	
	# read base config settings
	f = open( 'config_settings', 'r' )
	sleep	= f.readline().rstrip( '\n' )
	on		= f.readline().rstrip( '\n' )
	fire	= f.readline().rstrip( '\n' )
	
	# make sure settings were read from the config_settings file
	#
	#	- sometimes python reads the settings while php is truncating the file
	#		with file_put_contents() and before new settings have been written
	#
	if( sleep == '' or on == '' or fire == '' ):
		continue
	else:
		sleep = int( sleep )
		on = int( on )
		fire = int( fire )
	
	# system is off ( do not respond to motion )
	if sleep == 1:
		PWM.add_channel_pulse( 0, red_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 0 )
		time.sleep( 1 )
		continue
	
	# check for motion detection
	motion = RPIO.input( motion_gpio )
	print motion
	print motion_delay_cycles
	print num_motion_delay_cycles
	
	# check for motion
	#
	#	- read the motion gpio pin and set is_motion variable
	#
	if ( motion or motion_delay == 1 ) and on == 0 and sleep == 0:
	
		# delay off after motion is detected
		if( num_motion_delay_cycles > 0 and num_motion_delay_cycles < motion_delay_cycles ):
			motion_delay = 1
			num_motion_delay_cycles += 1;
		else:
			motion_delay = 0
			
		# reset cycle count if more motion is detected within the delay time
		if( motion ):
			num_motion_delay_cycles = 1
		
		# turn motion lights on
		PWM.add_channel_pulse( 0, red_gpio, 0, 500 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 200 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 300 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 100 )		
		
		# sleep cycle before continuing
		time.sleep( 0.1 )
		continue
	
	# stop motion delay if:
	#
	#	- no motion is detected and no motion delay has been triggered
	#	- motion delay cycle count reached without more motion being detected
	#	- lights were turned on
	#	- Natalia was put to sleep
	#
	else:
		motion_delay = 0
		num_motion_delay_cycles = 0
	
	# lights are turned off
	#
	#	- skip if motion is detected
	#
	if on == 0 and motion == 0:
		PWM.add_channel_pulse( 0, red_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 100 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 0 )
		time.sleep( 0.1 )
		continue
	
	# fire lighting
	#
	#
	#
	if fire == 1:
		
		# red ( primary fire color )
		red = 100
		red = red + random.randint( 0, 400 )
		PWM.add_channel_pulse( 0, red_gpio, 0, red )
		
		# green
		green = 10
		green = green + random.randint( 0, 20 )
		PWM.add_channel_pulse( 0, green_gpio, 0, green )
		
		# blue
		blue = 5
		blue = blue + random.randint( 0, 10 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, blue )
		
		# white
		white = 5
		white = white + random.randint( 0, 10 )
		PWM.add_channel_pulse( 0, white_gpio, 0, white )
		
		# sleep between changes
		seconds = 0.1
		seconds = seconds + random.randint( 0, 10 ) / 10
		time.sleep( seconds )
		continue
	
	# read color settings
	f = open( 'config_colors', 'r' )
	red_pw		= f.readline().rstrip( '\n' )
	green_pw	= f.readline().rstrip( '\n' )
	blue_pw		= f.readline().rstrip( '\n' )
	white_pw	= f.readline().rstrip( '\n' )

	# make sure colors were read from the config_colors file
	#
	#	- sometimes python reads the colors while php is truncating the file
	#		with file_put_contents() and before new colors have been written
	#
	if( red_pw == '' or green_pw == '' or blue_pw == '' or white_pw == '' ):
		continue
	else:
		red_pw = int( red_pw )
		green_pw = int( green_pw )
		blue_pw = int( blue_pw )
		white_pw = int( white_pw )

	# all cycles but the first ( that haven't already been intercepted by an if, above )
	#
	#	- first cycle runs a setup routine with pretty blinks and turns all pins on
	#
	
	# red
	if red_pw == 0:
		PWM.clear_channel_gpio( 0, red_gpio )
	else:
		PWM.add_channel_pulse( 0, red_gpio, 0, red_pw )

	# green
	if green_pw == 0:
		PWM.clear_channel_gpio( 0, green_gpio )
	else:
		PWM.add_channel_pulse( 0, green_gpio, 0, green_pw )

	# blue
	if blue_pw == 0:
		PWM.clear_channel_gpio( 0, blue_gpio )
	else:
		PWM.add_channel_pulse( 0, blue_gpio, 0, blue_pw )
	
	# white
	if white_pw == 0:
		PWM.clear_channel_gpio( 0, white_gpio )
	else:
		PWM.add_channel_pulse( 0, white_gpio, 0, white_pw )
	
	time.sleep( 0.1 )