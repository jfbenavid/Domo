<?php
	$estado = $_POST['estado'];
	$puerto = $_POST['puerto'];
	$tipo = $_POST['tipoConsul'];
	
	//buscar valor del dimmer puesto ya en la pagina
	if($puerto!=0){
		//conecta con MySql
		$con = mysqli_connect("localhost","root","") or die ("Fallo en la conexion!!");
		//Escoge la base de datos
		mysqli_select_db($con, "domotica") or die ("Fallo en seleccion de base de datos");
		//busca los datos del puerto que se envia
		$resultado = mysqli_query($con, "SELECT Puerto, Valor FROM Dimmer WHERE (Puerto = $puerto)") 
								or die ("Fallo en la consulta!");

		if($tipo == 1){//si consulta es para establecer valor de controles
			$reg = mysqli_fetch_array($resultado);
			echo $reg[1];
		}else{//si la consulta es para actualizar la bd
			$reg = mysqli_num_rows($resultado);
			if($reg != 0){
				mysqli_query($con, "UPDATE Dimmer SET Valor = $estado WHERE Puerto = $puerto")
							or die ("Fallo en el Update!");
			}
			else{
				mysqli_query($con, "INSERT INTO Dimmer (Puerto, Valor) VALUES ($puerto, $estado)")
							or die ("Fallo en el Insert!");
			}
			echo $estado;
		}
		mysqli_close($con);
		//ejectuta el archivo python del dimmer
		exec("sudo python /var/www/domo/python/dimmer.py $puerto $estado");
	}
	
?>
