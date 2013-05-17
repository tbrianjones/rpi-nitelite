<?php

	$start_time = microtime( TRUE );
	
	$cycles = 0;
	$time_elaspsed = 0;
	while( $time_elapsed < 10 ) {
		
		// calculate cycle times
		$cycles++;
		$now = microtime( TRUE );
		$time_elapsed = $now - $start_time;
		
	}
	
	$cycle_time = $time_elapsed / $cycles;
	
	echo "\n\n-- RESULTS -----------------";
	echo "\nElapsed Time: $elapsed_time";
	echo "\nCycles: $cycles";
	echo "\nCycle Time: $cycle_time";
	echo "\n\n";

?>