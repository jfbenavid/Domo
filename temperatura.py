def BinarioADecimal(sNum):
	return str(int(sNum, 2))

	data = []
	datos = {}
	bit_count = 0
	tmp = 0
	count = 0
	HumidityBit = ""
	TemperatureBit = ""
	crc = ""

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,GPIO.HIGH)
	time.sleep(0.025)
	GPIO.output(4,GPIO.LOW)
	time.sleep(0.02)

	GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

	for i in range(0,500):
	    data.append(GPIO.input(4))

	try:
		while data[count] == 1:
			tmp = 1
			count = count + 1

		for i in range(0, 32):
			bit_count = 0

			while data[count] == 0:
				tmp = 1
				count = count + 1

			while data[count] == 1:
				bit_count = bit_count + 1
				count = count + 1

			if bit_count > 3:
				if i >= 0 and i < 8:
					HumidityBit = HumidityBit + "1"
				if i >= 16 and i < 24:
					TemperatureBit = TemperatureBit + "1"
			else:
				if i >= 0 and i < 8:
					HumidityBit = HumidityBit + "0"
				if i >= 16 and i < 24:
					TemperatureBit = TemperatureBit + "0"

	except:
		print "ERR_RANGE"
		exit(0)

	try:
		for i in range(0, 8):
			bit_count = 0

			while data[count] == 0:
				tmp = 1
				count = count + 1

			while data[count] == 1:
				bit_count = bit_count + 1
				count = count + 1

			if bit_count > 3:
				crc = crc + "1"
			else:
				crc = crc + "0"
	except:
		print "ERR_RANGE"
		exit(0)

	datos['humedad'] = BinarioADecimal(HumidityBit)
	datos['Temperatura'] = BinarioADecimal(TemperatureBit)

	if int(datos['humedad']) + int(datos['Temperatura']) - int(BinarioADecimal(crc)) == 0:
		print "Humidity: " + datos['humedad'] + "%"
		print "Temperature: " + datos['Temperatura'] + "C"
		return datos
	else:
		print "ERR_CRC"
