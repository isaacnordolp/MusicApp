from pydub import AudioSegment

def changeSpeed(sound, speed=1.0):
    finalSound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return finalSound.set_frame_rate(sound.frame_rate)

#Crea una linea de musica
def createMusicLine():
    audioFinal = 0
    exit = 1
    while(exit==1):
        noteName = input("Inserta el nombre de la nota: ")
        noteDuration = int(input("Inserta la duración de la nota: "))
        route = 'Samples/'+durations.get(noteDuration)+'/' + noteName + '.wav' 
        audio = AudioSegment.from_file(route, format="wav")
        audioFinal += audio
        exit = int(input("Si quiere segir añadiendo, escriba 1, si ya termino, escriba 0: "))
    return audioFinal

def createMusicFile():
    newLine = 1
    audioArray = []

    while(newLine==1):
        audioArray.append(createMusicLine())
        newLine = int(input("Inserta 1 si quieres añadir otra linea musical o 0 si ya terminaste: "))
    
    audioFinal = audioArray[0]
    for i in range(1, len(audioArray)):
        audioFinal = audioFinal.overlay(audioArray[i], position=0)

    fileName = input("Inserta el nombre de tu cancion: ")
    audioFinal.export(fileName+'.wav', format="wav")

durations ={1:"whole", 2:"half", 4:"quarter", 8:"eigth"}
print("<<< MusicApp >>>")
createMusicFile()

#Changes speed (also changes pitch)
#fast = changeSpeed(half, 1.5)