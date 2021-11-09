import os

d =['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
for i in range(7):
	for j in range(12):
		numero = (12*i) + j
		numeroArchivo = f"{(2*numero) + 1:03d}"
		archivo = "Mi canción_"+numeroArchivo+'.wav'
		#print(archivo)
		nombre = d[j]+str(i)+".wav"
		#print(nombre)
		os.rename(archivo, nombre)

	
