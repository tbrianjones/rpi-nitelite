<?php

	// updates colors based on url parameters
	//
	//	- not a regular page for users
	//

	require_once( 'config.php' );

	ini_set( 'display_errors', 1 );
	error_reporting( E_ALL );

	if(
		isset( $_GET['r'] )
		OR isset( $_GET['g'] )
		OR isset( $_GET['b'] )
		OR isset( $_GET['w'] )
	) {
		
		$path = NITELITE_ROOT_PATH . 'pi/config_colors';
		
		// get array of current pulse widths settings for r,g,b,w
		$settings = explode( "\n", file_get_contents( $path ) );
		
		// process red
		if( isset( $_GET['r'] ) )
			$settings[0] = $_GET['r'];
			
		// process green
		if( isset( $_GET['g'] ) )
			$settings[1] = $_GET['g'];
			
		// process blue
		if( isset( $_GET['b'] ) )
			$settings[2] = $_GET['b'];
			
		// process white
		if( isset( $_GET['w'] ) )
			$settings[3] = $_GET['w'];
		
		// write new pulse widths
		file_put_contents( $path, implode( "\n", $settings ) );

		// redirect to menu
		header( 'Location: ' . NITELITE_ROOT_WWW );
			
	}

?>

<p>Colors must be specified<br />in the URL parameters.</p>
<p><a href="<?php echo NITELITE_ROOT_WWW; ?>">Go Home</a></p>