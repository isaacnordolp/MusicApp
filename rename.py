import os

names =['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
duration =['whole','half','quarter','eigth']
for k in range(4):
	for i in range(7):
		for j in range(12):
			numero = (12*i) + j
			numeroArchivo = f"{(2*numero) + 1:03d}"
			archivo = duration[k]+"/Mi canción_"+numeroArchivo+'.wav'
			#print(archivo)
			nombre = names[j]+str(i)+".wav"
			#print(nombre)
			os.rename(archivo, nombre)

	
