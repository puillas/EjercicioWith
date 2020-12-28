from io import open


with open("log.txt") as archivoLog:
	NumeroVecesError=0
	NumeroVecesNotice=0
	for line in archivoLog:
		if "[error]" in line:
			NumeroVecesError +=1
		elif "[notice]" in line:
			NumeroVecesNotice +=1
	LineasTotales = NumeroVecesError + NumeroVecesNotice
	PorcentajeError = NumeroVecesError / LineasTotales * 100
with open("resultado.txt", "w") as resultado:
	resultado.write("El archivo log tiene un " + str(PorcentajeError) + "%" + " de error")






