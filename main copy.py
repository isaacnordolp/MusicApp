from pydub import AudioSegment
import os

#Listas y diccionarios usados
notes =["C","D","E","F","G","A","B","C#","D#","F#","G#","A#"]
specialNotes = {"CB":"B","DB":"C#","EB":"D#","FB":"E","GB":"F#","AB":"G#","BB":"A#","B#":"C","E#":"F"}
durations ={'1':"whole", '2':"half", '2.':"whole", '4':"quarter",'4.':"half", '8':"eigth",'8.':"quarter",'16':"semiquaver" }
notValidString = "Entrada no válida"
forbiddenCharacters = ["\\", "/", ':', '*', '?', '"', '<', '>']

#Genera nombres únicos para guardar los archivos
def getUniqueName(fileName, format):
    finalName = fileName + format
    if(os.path.isfile(finalName)):
        i = 1
        while(os.path.isfile(finalName)):
            finalName = fileName + '(' + str(i) +')' + format
            i = i + 1
        return finalName
    else:
        return finalName

#Escribe la línea en que hay un error y termina el programa
def returnErrorLine(counter):
    return ("Hay un error en el archivo en la línea " + str(counter)) 

#Recibe y restringe las entradas del usuario
def getInput(status):
    global textInput
    global lineCounter
    if(textInput == 0):
        match status:
            case "instrument":
                while (True):
                    userIn = input("\nElige el instrumento para esta linea (P = piano, G = Guitarra, C = Cuerdas): ").upper()
                    if userIn == "HELP":
                        print("Los instrumentos que puedes elegir son:\nP = Piano\nG = Guitarra\nC = Cuerdas")
                    elif userIn == "P" or userIn == "G" or userIn == "C":
                        return userIn
                    else:
                        print(notValidString+": Instrumento no encontrado") 
            case "note":
                while (True):
                    notValid = False
                    userIn = input("\nInserta el nombre de la nota: ").upper()
                    if userIn == "S":
                        return userIn
                    elif len(userIn) == 2:
                        note = userIn[0]
                    elif len(userIn) == 3:
                        note = userIn[0:2]
                    try:
                        octave = int(userIn[-1]) 
                        if(note not in notes and note not in specialNotes) or octave > 7 or octave < 1:
                            notValid = True  
                    except:
                        notValid = True              
                    if userIn == "HELP":
                        print("Debes ingresar una nota siguiendo: Nota+Octava. Como por ejemplo: C#4 o Db4.\nNombres de notas: B#/C  C#/Db  D  D#/Eb  E/Fb  E#/F  F#/Gb  G  G#/Ab  A  A#/Bb  B/Cb\nPara insertar un silencio, escribe 'S'")
                    elif notValid or userIn == "B#7" or userIn == "CB1":
                        print(notValidString+": Nota no válida")
                    else: 
                        if note in notes:
                            if note == "B#":
                                return note + str(octave+1)
                            else:
                                return note + str(octave)
                        elif note in specialNotes:
                            if note == "CB":
                                return specialNotes.get(note) + str(octave-1)
                            else:
                                return specialNotes.get(note) + str(octave)
            case "duration":
                while (True):
                    userIn = input("Inserta la duración de la nota: ").upper()
                    if userIn == "HELP":
                        print("Puedes ingresar una de las siguientes duraciones:\n1 (redonda)\n2 (blanca)\n2. (blanca con punto)\n4 (negra)\n4. (negra con punto)\n8 (corchea)\n8. (corchea con punto)\n16 (semicorchea)\n")
                    elif(userIn in durations):
                        return userIn
                    else:
                        print(notValidString+": Duración no válida\n")
            case "nextNote":
                while(True):
                    userIn = input("\nPara añadir otra nota en esta línea escribe 1, si no, escribe 0: ")
                    if(userIn == '1' or userIn == '0'):
                        return userIn
                    else:
                        print(notValidString)
            case "nextLine":
                while(True):
                    userIn = input("\nPara añadir otra linea musical escribe 1, si no, escribe 0: ")
                    if(userIn == '1' or userIn == '0'):
                        return userIn
                    else:
                        print(notValidString)
            case "nextAction":
                while(True):
                    userIn = input("Inserta:\n'A' para crear un archivo de audio\n'T' para crear un archivo de texto\n'G' para generar un audio a partir de un archivo .matf\n'F' para finalizar el programa\n").upper()
                    if(userIn == 'A' or userIn == 'G' or userIn == 'T' or userIn == 'F'):
                        return userIn
                    else:
                        print(notValidString+": Acción no válida")
            case "tempo":
                while(True):
                    userIn = input("\nInserta el tempo (BPM) de la pieza: ")
                    notValid = False
                    if userIn == "HELP":
                        print("Inserta un tempo, expresado en BPM. Sus valores aceptados van de 60 a 240")
                    else:
                        try:
                            userIn = int(userIn)
                            if(userIn < 60 or userIn >240):
                                notValid = True
                        except:
                            notValid = True
                        if notValid:
                            print(notValidString+": Tempo no válido")
                        else: 
                            return userIn
            case "title":
                while(True):
                    userIn = input("\nInserta el nombre de la pieza: ").strip()
                    notValid = False
                    if userIn == '':
                        notValid = True
                    else:
                        for i in range(len(userIn)):
                            if userIn[i] in forbiddenCharacters:
                                notValid = True
                                break
                    if userIn.upper() == "HELP":
                        print("No puedes usar estos caracteres: \, /, :, *, ?, \", <, >, |")
                    elif notValid:
                        print(notValidString+": Inserta un nombre válido")
                    else: 
                        return userIn
    elif(textInput == 1):
        match status:
            case "instrument":
                userIn = file.readLine()
                lineCounter +=  1
                if userIn == "P" or userIn == "G" or userIn == "C":
                    return userIn
                else:
                    raise Exception(returnErrorLine(lineCounter))

            case "note":
                notValid = False
                userIn = file.readLine().upper()
                lineCounter += 1
                if len(userIn) == 2:
                    note = userIn[0]
                elif len(userIn) == 3:
                    note = userIn[0:2]
                try:
                    octave = int(userIn[-1]) 
                    if(note not in notes and note not in specialNotes) or octave > 7 or octave < 1:
                        notValid = True  
                except:
                    notValid = True              
                if notValid:
                    raise Exception(returnErrorLine(lineCounter))
                else: 
                    if note in notes:
                        return note + str(octave)
                    elif note in specialNotes:
                        return specialNotes.get(note) + octave
            case "duration":
                userIn = file.readLine()
                lineCounter += 1
                if(userIn in durations):
                    return userIn
                else:
                    raise Exception(returnErrorLine(lineCounter))
            case "nextNote":
                userIn = file.readLine()
                lineCounter += 1
                if(userIn == '1' or userIn == '0'):
                    return userIn
                else:
                    raise Exception(returnErrorLine(lineCounter))
            case "nextLine":
                userIn = file.readLine()
                lineCounter += 1
                if(userIn == '1' or userIn == '0'):
                    return userIn
                else:
                    raise Exception(returnErrorLine(lineCounter))

            case "tempo":
                notValid = False
                try:
                    userIn = int(file.readLine())
                    lineCounter += 1
                    if(userIn < 60 or userIn >240):
                        notValid = True
                except:
                    notValid = True
                if notValid:
                    raise Exception(returnErrorLine(lineCounter))
                else: 
                    return userIn
            case "title":
                notValid = False
                userIn = file.readLine().strip()
                lineCounter += 1
                if userIn == '':
                    notValid = True
                else:
                    for i in range(len(userIn)):
                        if userIn[i] in forbiddenCharacters:
                            notValid = True
                            break
                if notValid:
                    raise Exception(returnErrorLine(lineCounter))
                else: 
                    return userIn
     
#Cambia la velocidad del audio
def changeSpeed(sound, speed):
    finalSound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return finalSound.set_frame_rate(sound.frame_rate)

#Clase para hacer listas enlazadas con las notas
class NoteNode:
    def __init__(self):
        #data de la nota
        self.noteName = getInput("note")
        self.noteDuration = getInput("duration")

        #pointer anterior
        self.previous = None

        #pointer siguiente
        self.next = None
    def hasNext(self):
        return self.next!=None;
    def hasPrevious(self):
        return self.previous!=None;

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,nuevoNodo):
        if self.head==None:
            #Si no hay head, se crea el primero
            self.head == nuevoNodo
        else:
            #De lo contrario, se itera iniciando con el nodo head
            temporalNode = self.head
            while temporalNode.next!=None:
                temporalNode = temporalNode.next
            nuevoNodo.previous = temporalNode
            temporalNode.next = nuevoNodo

class Stack:
    def __init__(self):
        self.notes = []
    def isEmpty(self):
        return self.notes == []
    def add(self, elem):
        self.notes.append(elem)
    def remove(self):
        return self.notes.pop()
    





#Crea una linea de musica
def createMusicLine():
    instrument = getInput("instrument")
    audioFinal = 0
    exit = 1
    while(exit==1):
        noteName = getInput("note")
        noteDuration = getInput("duration")
        route = 'Samples/'+ instrument +'/'+durations.get(noteDuration)+'/' + noteName + '.wav' 
        audio = AudioSegment.from_file(route, format="wav")
        #Esto es para las duraciones intermedias
        if (noteDuration == '2.'):
            audio = audio[0:1500]
        elif (noteDuration == '4.'):
            audio = audio[0:750]
        elif (noteDuration == '8.'):
            audio = audio[0:375]
        audioFinal += audio
        exit = int(getInput("nextNote"))
    return audioFinal

#Crea el archivo de musica
def createMusicFile():
    newLine = 1
    audioArray = []
    fileName = getInput("title")
    tempo = getInput("tempo")/120
    while(newLine==1):
        audioArray.append(createMusicLine())
        newLine = int(getInput("nextLine"))
    audioFinal = audioArray[0]
    for i in range(1, len(audioArray)):
        audioFinal = audioFinal.overlay(audioArray[i], position=0)
    audioFinal = changeSpeed(audioFinal, tempo)
    finalName = getUniqueName(fileName, ".wav")
    audioFinal.export(finalName, format="wav")
    print('Tu obra "'+ finalName + '" fue guardada con éxito.')

#Crea una linea de texto
def createTextLine(textFile):
    instrument = getInput("instrument")
    textFile.write(instrument+"\n")
    exit = 1
    while(exit==1):
        noteName = getInput("note")
        textFile.write(noteName+"\n")
        noteDuration = getInput("duration")
        textFile.write(noteDuration+"\n")
        exit = int(getInput("nextNote"))
        textFile.write(str(exit)+"\n")

#Crea el archivo de texto
def createTextFile():
    newLine = 1
    fileName = getInput("title")
    finalName = getUniqueName(fileName, ".matf")
    textFile= open(finalName,"w+")
    textFile.write(fileName+"\n")
    tempo = str(getInput("tempo"))
    textFile.write(tempo+"\n")
    while(newLine==1):
        createTextLine(textFile)
        newLine = int(getInput("nextLine"))
        textFile.write(str(newLine)+"\n")
    textFile.close()
    print('Tu obra "'+ finalName + '" fue guardada con éxito.')

global textInput
textInput = 0
global lineCounter
print("--------------------------")
print("♪ BIENVENIDO A MUSIC APP ♪")
print("--------------------------")
action = ""
while(action != 'F'):
    action = getInput("nextAction")
    if action == "A":
        textInput = 0
        createMusicFile()
    elif action == "T":
        createTextFile()
    elif action == "G":
        textInput = 1
        lineCounter = 0
        try:
            while(True):
                textFile = input("Introduzca la ruta del archivo '.matf': ")
                if(os.path.isfile(textFile) and textFile[-5:] == ".matf"):
                    file = open(textFile,"r")
                    break
                else:
                    print("La ruta y/o el archivo no son válidos")
            print("Hola")
            createMusicFile()
        except:
            pass

