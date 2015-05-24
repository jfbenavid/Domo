<?php
	$estado = $_POST['estado'];
	$puerto = $_POST['puerto'];
	$tipo = $_POST['tipoConsul'];
	//escribe en el archivo txt el valor del estado del dimmer
	//$file = '../txt/estado.txt';
	//file_put_contents($file, $estado);

	//buscar valor del dimmer puesto ya en la pagina
	$con = mysql_connect("localhost","root","123456") or die ("Fallo en la conexion!!");
	mysql_select_db("domotica", $con) or die ("Fallo en seleccion de base de datos");
	$resultado = mysql_query("SELECT Puerto, Valor FROM Dimmer WHERE (Puerto = $puerto)", $con) 
						or die ("Fallo en la consulta!");

	if($tipo = 1){//si consulta es para establecer valor de controles
		$reg = mysql_fetch_array($resultado);
		echo $reg['Valor'];
	}else{//si la consulta es para actualizar la bd
		if($reg = mysql_fetch_array($resultado)){
			mysql_query("UPDATE Dimmer SET Valor = $estado WHERE Puerto = $puerto", $con)
						or die ("Fallo en el Update!");
		}
		else{
			mysql_query("INSERT INTO Dimmer (Puerto, Valor) VALUES ($puerto, $estado)", $con)
						or die ("Fallo en el Insert!");
		}
	}
	
	mysql_close($con);
	//ejectuta el archivo python del dimmer
	exec('sudo python /var/www/domo/python/dimmer.py $estado');

?>
