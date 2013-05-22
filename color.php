<?php require( 'header.php' ); ?>

<?php

	ini_set( 'display_errors', 1 );
	error_reporting( E_ALL );

	if(
		isset( $_GET['r'] )
		OR isset( $_GET['g'] )
		OR isset( $_GET['b'] )
		OR isset( $_GET['w'] )
	) {
		
		$pulse_width_file_path = NITELITE_ROOT_PATH . 'pi/pulse_widths';
		
		// get array of pulse widths for r,g,b,w
		$pulse_widths = explode( file_get_contents( $pulse_width_file_path ), "\n" );
		
		// process red
		if( isset( $_GET['r'] ) )
			$pulse_widths[0] = $_GET['r'];
			
		// process green
		if( isset( $_GET['g'] ) )
			$pulse_widths[1] = $_GET['g'];
			
		// process blue
		if( isset( $_GET['b'] ) )
			$pulse_widths[2] = $_GET['b'];
			
		// process white
		if( isset( $_GET['w'] ) )
			$pulse_widths[3] = $_GET['w'];
		
		// write new pulse widths
		file_put_contents( $pulse_width_file_path, implode( "\n", $pulse_widths ) );

		// redirect to menu
		header( 'Location: ' . NITELITE_ROOT_WWW );
			
	}

?>

	<ul>
		<li><a href="?r=500&g=500&b=500&w=500">BRIGHT</a></li>
		<li><a href="?r=500&g=0&b=0&w=0">RED</a></li>
		<li><a href="?r=500&g=100&b=0&w=0">ORANGE</a></li>
		<li><a href="?r=500&g=200&b=0&w=0">YELLOW</a></li>
		<li><a href="?r=0&g=500&b=0&w=0">GREEN</a></li>
		<li><a href="?r=0&g=0&b=500&w=0">BLUE</a></li>
		<li><a href="?r=500&g=0&b=250&w=0">VIOLET</a></li>
		<li><a href="?r=0&g=0&b=0&w=500">WHITE</a></li>
	</ul>

<?php require( 'footer.php' ); ?>