# import required python libraries
import RPIO.PWM as PWM
import time as time
import random

# gpio pins
red_gpio	= 23
green_gpio	= 24
blue_gpio	= 25
white_gpio	= 22

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
	sleep				= int( f.readline().rstrip( '\n' ) )
	on					= int( f.readline().rstrip( '\n' ) )
	fire				= int( f.readline().rstrip( '\n' ) )
	
	# system is off ( do not respond to motion )
	if sleep == 1:
		PWM.add_channel_pulse( 0, red_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 0 )
		time.sleep( 0.5 )
		continue
	
	# check for motion
	#
	#	- read the motion gpio pin and set is_motion variable
	#
	motion = 0
	if motion == 1:
		PWM.add_channel_pulse( 0, red_gpio, 0, 500 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 250 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 250 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 100 )
		time.sleep( 0.5 )
		continue
	
	# lights are turned off
	#
	#	- skip if motion is detected
	#
	if on == 0 and motion == 0:
		PWM.add_channel_pulse( 0, red_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, green_gpio, 0, 100 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, 0 )
		PWM.add_channel_pulse( 0, white_gpio, 0, 0 )
		time.sleep( 0.5 )
		continue
	
	# fire lighting
	#
	#
	#
	if fire == 1:
		
		# red ( primary fire color )
		red = 50
		red = red + random.randint( 0, 450 )
		PWM.add_channel_pulse( 0, red_gpio, 0, red )
		
		# green
		green = 3
		green = green + random.randint( 0, 20 )
		PWM.add_channel_pulse( 0, green_gpio, 0, green )
		
		# blue
		blue = 1
		blue = blue + random.randint( 0, 10 )
		PWM.add_channel_pulse( 0, blue_gpio, 0, blue )
		
		# white
		white = 1
		white = white + random.randint( 0, 10 )
		PWM.add_channel_pulse( 0, white_gpio, 0, white )
		
		# sleep between changes
		seconds = 0.2
		seconds = seconds + random.randint( 0, 20 ) / 10
		time.sleep( seconds )
		continue
	
	# read custom color settings
	f = open( 'config_colors', 'r' )
	custom_red_pw		= int( f.readline().rstrip( '\n' ) )
	custom_green_pw		= int( f.readline().rstrip( '\n' ) )
	custom_blue_pw		= int( f.readline().rstrip( '\n' ) )
	custom_white_pw		= int( f.readline().rstrip( '\n' ) )
			
	# all cycles but the first ( that haven't already been intercepted by an if, above )
	#
	#	- first cycle runs a setup routine with pretty blinks and turns all pins on
	#
	
	# red
	if custom_red_pw == 0:
		PWM.clear_channel_gpio( 0, red_gpio )
	else:
		PWM.add_channel_pulse( 0, red_gpio, 0, custom_red_pw )

	# green
	if custom_green_pw == 0:
		PWM.clear_channel_gpio( 0, green_gpio )
	else:
		PWM.add_channel_pulse( 0, green_gpio, 0, custom_green_pw )

	# blue
	if custom_blue_pw == 0:
		PWM.clear_channel_gpio( 0, blue_gpio )
	else:
		PWM.add_channel_pulse( 0, blue_gpio, 0, custom_blue_pw )
	
	# white
	if custom_white_pw == 0:
		PWM.clear_channel_gpio( 0, white_gpio )
	else:
		PWM.add_channel_pulse( 0, white_gpio, 0, custom_white_pw )
	
	time.sleep( 0.5 )