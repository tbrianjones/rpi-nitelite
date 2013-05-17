Nite-Lite
=========


utilities
---------

### wiringPi
- download and install: https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
- operation
	- man gpio
	- couldn't get the software PWM working.  I don't think the GPIO CLI utility has softPWM built in yet.

### RPIO
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
