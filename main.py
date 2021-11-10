from pydub import AudioSegment

#Cambia la velocidad del archivo
def changeSpeed(sound, speed=1.0):
    finalSound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return finalSound.set_frame_rate(sound.frame_rate)

#Crea una linea de musica
def createMusicLine():
    instrument = input("Elige el instrumento para esta linea (P = piano, G = Guitarra): ")
    audioFinal = 0
    exit = 1
    while(exit==1):
        noteName = input("Inserta el nombre de la nota: ")
        if len(noteName) == 3 and noteName[1] == 'b':
            octave = noteName[2]
            noteName = noteName[0:2]
            noteName = specialNotes.get(noteName) + octave
        noteDuration = int(input("Inserta la duración de la nota: "))
        route = 'Samples/'+ instrument +'/'+durations.get(noteDuration)+'/' + noteName + '.wav' 
        audio = AudioSegment.from_file(route, format="wav")
        audioFinal += audio
        exit = int(input("Para añadir otra nota escribe 1, si no, escribe 0: "))
    return audioFinal

#Crea el archivo de musica
def createMusicFile():
    finish = 1
    while(finish ==1):
        newLine = 1
        audioArray = []

        while(newLine==1):
            audioArray.append(createMusicLine())
            newLine = int(input("Para añadir otra linea musical escribe 1, si no, escribe 0: "))
        
        audioFinal = audioArray[0]
        for i in range(1, len(audioArray)):
            audioFinal = audioFinal.overlay(audioArray[i], position=0)
        tempo = int(input("Inserta el tempo (BPM) de la pieza: "))/120
        audioFinal = changeSpeed(audioFinal, tempo)
        fileName = input("Inserta el nombre de la pieza: ")
        audioFinal.export(fileName+'.wav', format="wav")
        finish = int(input('Tu obra "'+ fileName + '.wav" fue guardada con éxito.\nPara crear una nueva obra, presiona 1. Para finalizar presiona 0: '))

durations ={1:"whole", 2:"half", 4:"quarter", 8:"eigth"}
specialNotes = {'Db':'C#','Eb':'D#','Gb':'F#','Ab':'G#','Bb':'A#'}
print("--------------------------")
print("♪ BIENVENIDO A MUSIC APP ♪")
print("--------------------------")
createMusicFile()