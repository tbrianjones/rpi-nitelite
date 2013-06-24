<?php

	require( 'header.php' );
	
	// get current settings
	$path = NITELITE_ROOT_PATH . 'pi/config_settings';
	$settings = explode( "\n", file_get_contents( $path ) );
	
?>

<style>

	table {
		width: 100%;
		border-bottom: 1px solid #ccc;
	}
	table tr td {
		width: 33%;
	}
	table tr td a {
		display: block;
		padding: 30px 0;
		text-align: center;
	}

</style>

<body>

	<ul>
		<?php
		
			// sleep / wake
			if( $settings[0] )
				echo '<li><a href="update_settings.php?sleep=0">WAKE</a></li>';
			else
				echo '<li><a href="update_settings.php?sleep=1">SLEEP</a></li>';
		
			// light on / lights off
			if( $settings[1] )
				echo '<li><a href="update_settings.php?on=0">LIGHTS OFF</a></li>';
			else
				echo '<li><a href="update_settings.php?on=1">LIGHTS ON</a></li>';
				
			// fire lighting / normal lighting
			if( $settings[2] )
				echo '<li><a href="update_settings.php?fire=0">MONOCHROME LIGHTING</a></li>';
			else
				echo '<li><a href="update_settings.php?fire=1">FIRE LIGHTING</a></li>';
		
		?>
	</ul>
	
	<?php if( ! $settings[2] ) { ?>
	
		<table>
			<tr>
				<td style="background-color: red;"><a href="update_colors.php?r=500&g=0&b=0&w=0">&nbsp;</a></td>
				<td style="background-color: orange;"><a href="update_colors.php?r=500&g=100&b=0&w=0">&nbsp;</a></td>
				<td style="background-color: yellow;"><a href="update_colors.php?r=500&g=200&b=0&w=0">&nbsp;</a></td>
			</tr>
			<tr>
				<td style="background-color: green;"><a href="update_colors.php?r=0&g=500&b=0&w=0">&nbsp;</a></td>
				<td style="background-color: blue;"><a href="update_colors.php?r=0&g=0&b=500&w=0">&nbsp;</a></td>
				<td style="background-color: purple;"><a href="update_colors.php?r=500&g=0&b=250&w=0">&nbsp;</a></td>
			</tr>
			<tr>
				<td style="background-color: white;"><a href="update_colors.php?r=0&g=0&b=0&w=500">&nbsp;</a></td>
				<td style="background-color: #fcfdeb;"><a href="update_colors.php?r=500&g=100&b=0&w=500">&nbsp;</a></td>
				<td style="background-color: #ebf3fd;"><a href="update_colors.php?r=100&g=0&b=100&w=500">&nbsp;</a></td>
			</tr>
		</table>
		
	<?php } ?>

</body>

<?php require( 'footer.php' ); ?>