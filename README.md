Raspberry-Pi Nitelite ( codename: Natalia )
===========================================


build
-----
- raspberry pi rev b
- motion sensor: http://www.parallax.com/Portals/0/Downloads/docs/prod/sens/555-28027-PIRSensor-v2.2.pdf
- custom built led board
	

setup pi
--------

### hardware
- install raspian on memory card
- install wireless network device

### software
- install apache
- install php
- install python
	- python utilities

### operating the nitelite
- boot the pi
- `sudo python the_brain.py`
	- this runs continuously and manages Natalia's inputs
	- this must be run as root ( using sudo ) so that the GPIO library can access the GPIO pins


config file notes
-----------------

- add notes about pulse widths
	- what are the current limits ( currently 0 to 500, 0 is off, 500 is max )
	- how are the limits determined

### config ( booleans, 0 or 1 )
- leds_off				turn leds on or off
- is_default			use default settings
- is_fire				use fire mode ( flickering fire effect )

### config_colors
- custom_red_pw			custom red pulse width
- custom_green_pw		custom green pulse width
- custom_blue_pw		custom blue pulse width
- custom_white_pw		custom white pulse width


utilities used
--------------

### RPIO ( in use by Natalia )
- useful blog post: http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=36670
- website: http://pythonhosted.org/RPIO/
- docs: https://github.com/metachris/RPIO/tree/master/documentation/source
- repo: https://github.com/metachris/RPIO
- install guide ( was missing a few things in docs )
	- $ sudo apt-get update ( needed to update stuff )
	- $ sudo apt-get install python-dev ( need the python dev package to run the setup.py file ... which compiles stuff )
	- $ git clone https://github.com/metachris/RPIO.git
	- $ cd RPIO
	- $ sudo python setup.py install
	- verified as working: tbj 10.05.13

### wiringPi ( not uing this )
- download and install: https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
- operation
	- man gpio
	- couldn't get the software PWM working.  I don't think the GPIO CLI utility has softPWM built in yet.

### viewport sensing in the web app
- https://developer.mozilla.org/en-US/docs/Mozilla/Mobile/Viewport_meta_tag
