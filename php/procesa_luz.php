<?php
	$valEstado=$_POST['est'];
	$numPuerto = $_POST['port'];

	if($valEstado == 1)
		$valEstado = 1;
	else
		$valEstado = "";
	
    exec("sudo python /var/www/domo/python/luz.py $numPuerto $valEstado");
    echo "sudo python /var/www/domo/python/luz.py $numPuerto $valEstado";
?>
