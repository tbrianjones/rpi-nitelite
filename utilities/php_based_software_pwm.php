<?php

	// php software based pwm for raspberry pi
	//
	// NOTES
	//
	//	- php is not able to maintain a steady enough clock
	//	- led's controlled with this flicker like crazy
	//

	// include rpi gpio library
	require_once( 'libraries/php-gpio-v1/GPIO.php' );
	$Gpio = new GPIO();
	$Gpio->setup( 25, "out" );

	// data to calculate cycle times
	$start_time = microtime( TRUE );
	$cycles = 0;
	$time_elaspsed = 0;
	
	// loop to do stuff during each cycle
	while( $time_elapsed < 1000 ) {
		
		// read pulse width from file
		if( $cycles === 0 OR $cycles % 50 === 0 )
			$pulse_width = trim( file_get_contents( 'pulse_width' ) );
			
		// track cycle time data
		echo "\nCurrent Cycle Time: " . ( $now - microtime( TRUE ) );
		$cycles++;
		$now = microtime( TRUE );
		$time_elapsed = $now - $start_time;

		// trigger led pulse
		$Gpio->output( 25, 1 );
		usleep( $pulse_width );
		$Gpio->output( 25, 0 );
		
		usleep( 8000 - $pulse_width );
				
	}
	
	// calculate and output results
	$cycle_time = $time_elapsed / $cycles;
	echo "\n\n-- RESULTS -----------------";
	echo "\nElapsed Time: $elapsed_time";
	echo "\nCycles: $cycles";
	echo "\nCycle Time: $cycle_time";
	echo "\n\n";

?>