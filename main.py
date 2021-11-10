from pydub import AudioSegment

#Recibe la entrada del usuario
notes =["A","B","C","D","E","F","G"]
notValidString = "Entrada no válida"
def getInput(status):
    statusList = ["instrument","note","duration","nextState"]
    match status:
        case "instrument":
            while (True):
                userIn = input("\nElige el instrumento para esta linea (P = piano, G = Guitarra): ").upper()
                if userIn == "help":
                    print("Los instrumentos que puedes elegir son:\nP = Piano\nG = Guitarra")
                elif userIn == "P" or userIn == "G":
                    return userIn
                else:
                    print(notValidString+": "+"Instrumento no encontrado") 
        case "note":
            while (True):
                userIn = input("\nInserta el nombre de la nota: ")
                lUserIn= len(userIn)
                notValid = False
                noteIn = userIn[0]
                octaveIn = userIn[-1]
                try:
                    noteIndex = notes.index(noteIn)
                    octave = int(octaveIn)
                    
                except:
                    notValid = True
                if userIn == "help":
                    print("Debes ingresar una nota siguiendo: NombreNota+Octava. Como por ejemplo: C#4 o Db4.\n Nombres de notas: C   C#/Db  D   D#/Eb  E   F   F#/Gb  G   G#/Ab  A   A#/Bb  B")
                elif notValid or octave > 7 or octave < 1:
                    print(notValidString+": "+"Octava o Nota no válida")

                elif lUserIn ==2:
                    return userIn
                elif lUserIn == 3:  
                    if userIn[1] == "#":
                        if noteIndex != 1 and noteIndex != 4:
                            return userIn
                        else: 
                            print(notValidString+": "+"Sostenido no válido")
                    elif userIn[1] == "b":
                        if noteIndex != 2 and noteIndex != 5:

                            return notes[noteIndex-1]+ "#" + octaveIn
                        else:
                            print(notValidString+": "+"Bemol no válido")
                else:
                    print (notValidString) 

        case "duration":
            return 3
        case "nextState":
            return 4


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
        #Permite insertar los bemoles también
        if len(noteName) == 3 and noteName[1] == 'b':
            octave = noteName[2]
            noteName = noteName[0:2]
            noteName = specialNotes.get(noteName) + octave
        noteDuration = input("Inserta la duración de la nota: ")
        #Esto es para las duraciones intermedias
        if (noteDuration == '2.'):
            route = 'Samples/'+ instrument +'/whole/' + noteName + '.wav' 
            audio = AudioSegment.from_file(route, format="wav")
            audio = audio[0:1500]
        elif (noteDuration == '4.'):
            route = 'Samples/'+ instrument +'/half/' + noteName + '.wav' 
            audio = AudioSegment.from_file(route, format="wav")
            audio = audio[0:750]
        #Esto es para las duraciones normales
        else:
            route = 'Samples/'+ instrument +'/'+durations.get(noteDuration)+'/' + noteName + '.wav' 
            audio = AudioSegment.from_file(route, format="wav")
        audioFinal += audio
        exit = int(input("\nPara añadir otra nota en esta línea escribe 1, si no, escribe 0: "))
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

durations ={'1':"whole", '2':"half", '4':"quarter", '8':"eigth"}
specialNotes = {'Db':'C#','Eb':'D#','Gb':'F#','Ab':'G#','Bb':'A#'}
print("--------------------------")
print("♪ BIENVENIDO A MUSIC APP ♪")
print("--------------------------")
action = ""
while(action != 'F'):
    action = input("\nInserta:\n'A' para crear un archivo de audio\n'T' para crear un archivo de texto\n'F' para finalizar el programa\n")
    if action == "A":
        createMusicFile()
    elif action == "T":
        createTextFile()