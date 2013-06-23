<?php

	// updates settings based on url parameters
	//
	//	- not a regular page for users
	//

	require_once( 'config.php' );

	ini_set( 'display_errors', 1 );
	error_reporting( E_ALL );

	if(
		isset( $_GET['sleep'] )
		OR isset( $_GET['on'] )
		OR isset( $_GET['fire'] )
	) {
		
		$path = NITELITE_ROOT_PATH . 'pi/config_settings';
		$settings = explode( "\n", file_get_contents( $path ) );
		
		// sleep / wake
		if( isset( $_GET['sleep'] ) )
			$settings[0] = $_GET['sleep'];
			
		// on / off
		if( isset( $_GET['on'] ) )
			$settings[1] = $_GET['on'];
			
		// fire / normal
		if( isset( $_GET['fire'] ) )
			$settings[2] = $_GET['fire'];
		
		// write new pulse widths
		file_put_contents( $path, implode( "\n", $settings ) );

		// redirect to menu
		header( 'Location: ' . NITELITE_ROOT_WWW );
			
	}

?>

<p>Settings must be specified<br />in the URL parameters.</p>
<p><a href="<?php echo NITELITE_ROOT_WWW; ?>">Go Home</a></p>