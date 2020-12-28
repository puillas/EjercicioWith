from io import open

archivoLog=open("log.txt")
textoEnLog=archivoLog
NumeroVecesError=0
NumeroVecesNotice=0
for line in textoEnLog:
	if "[error]" in line:
		NumeroVecesError +=1
	elif "[notice]" in line:
		NumeroVecesNotice +=1
LineasTotales = NumeroVecesError + NumeroVecesNotice
PorcentajeError = NumeroVecesError / LineasTotales * 100
archivoLog.close()
#------------CREACION DEL NUEVO ARCHIVO CON EL RESULTADO------

archivoResultado=open("resultado.txt", "w")

archivoResultado.write("El porcentaje de error del archivo log es " + str(PorcentajeError) + "%")

archivoResultado.close()

