<?php
	$valEstado = $_POST['est'];
	$numPuerto = $_POST['port'];

	if($valEstado == 1)
		$valEstado = 1;
	else
		$valEstado = 2;
	
    exec("sudo python /var/www/domo/python/luz.py $numPuerto $valEstado");
?>
