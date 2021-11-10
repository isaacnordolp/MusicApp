from pydub import AudioSegment

#Cambia la velocidad del archivo
def changeSpeed(sound, speed=1.0):
    finalSound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return finalSound.set_frame_rate(sound.frame_rate)

#Crea el archivo de musica
def createMusicFile():
    newLine = 1
    audioArray = []
    fileName = input("\nInserta el nombre de la pieza: ")
    tempo = int(input("Inserta el tempo (BPM) de la pieza: "))/120
    while(newLine==1):
        audioArray.append(createMusicLine())
        newLine = int(input("\nPara añadir otra linea musical escribe 1, si no, escribe 0: "))
    audioFinal = audioArray[0]
    for i in range(1, len(audioArray)):
        audioFinal = audioFinal.overlay(audioArray[i], position=0)
    audioFinal = changeSpeed(audioFinal, tempo)
    audioFinal.export(fileName+'.wav', format="wav")
    print('Tu obra "'+ fileName + '.wav" fue guardada con éxito.')

#Crea una linea de musica
def createMusicLine():
    instrument = input("\nElige el instrumento para esta linea (P = piano, G = Guitarra): ")
    audioFinal = 0
    exit = 1
    while(exit==1):
        noteName = input("\nInserta el nombre de la nota: ")
        if len(noteName) == 3 and noteName[1] == 'b':
            octave = noteName[2]
            noteName = noteName[0:2]
            noteName = specialNotes.get(noteName) + octave
        noteDuration = int(input("Inserta la duración de la nota: "))
        route = 'Samples/'+ instrument +'/'+durations.get(noteDuration)+'/' + noteName + '.wav' 
        audio = AudioSegment.from_file(route, format="wav")
        audioFinal += audio
        exit = int(input("\nPara añadir otra nota escribe 1, si no, escribe 0: "))
    return audioFinal

#Crea el archivo de texto
def createTextFile():
    newLine = 1
    fileName = input("\nInserta el nombre de la pieza: ")
    textFile= open(fileName+".txt","w+")
    textFile.write(fileName+"\n")
    tempo = input("Inserta el tempo (BPM) de la pieza: ")
    textFile.write(tempo+"\n")
    while(newLine==1):
        createTextLine(textFile)
        newLine = int(input("\nPara añadir otra linea musical escribe 1, si no, escribe 0: "))
        textFile.write(str(newLine)+"\n")
    textFile.close()
    print('Tu obra "'+ fileName + '.txt" fue guardada con éxito.')

#Crea una linea de texto
def createTextLine(textFile):
    instrument = input("\nElige el instrumento para esta linea (P = piano, G = Guitarra): ")
    textFile.write(instrument+"\n")
    exit = 1
    while(exit==1):
        noteName = input("\nInserta el nombre de la nota: ")
        textFile.write(noteName+"\n")
        noteDuration = input("Inserta la duración de la nota: ")
        textFile.write(noteDuration+"\n")
        exit = int(input("\nPara añadir otra nota escribe 1, si no, escribe 0: "))
        textFile.write(str(exit)+"\n")

durations ={1:"whole", 2:"half", 4:"quarter", 8:"eigth"}
specialNotes = {'Db':'C#','Eb':'D#','Gb':'F#','Ab':'G#','Bb':'A#'}
print("--------------------------")
print("♪ BIENVENIDO A MUSIC APP ♪")
print("--------------------------")
action = ""
while(action != '0'):
    action = input("\nInserta:\n'A' para crear un archivo de audio\n'T' para crear un archivo de texto\n'0' para finalizar el programa\n")
    if action == "A":
        createMusicFile()
    elif action == "T":
        createTextFile()