from pydub import AudioSegment

def speed_change(sound, speed=1.0):
    finalSound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return finalSound.set_frame_rate(sound.frame_rate)


whole = AudioSegment.from_file("Samples\whole\C0.wav" , format="wav")
half = AudioSegment.from_file("Samples\half\C0.wav" , format="wav")
quarter = AudioSegment.from_file("Samples\quarter\C0.wav" , format="wav")
eigth = AudioSegment.from_file("Samples\eigth\C0.wav" , format="wav")

#Combines 2 audios into one
overlay = whole.overlay(half, position=0)

#Changes speed (also changes pitch)
fast = speed_change(half, 1.5)

#Joins 2 or more audios
combineWhole = whole+whole
combineHalf = half+half+half+half
combineQuarter = quarter+quarter+quarter+quarter+quarter+quarter+quarter+quarter
combineEigth = eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth+eigth


#Exports the results
overlay.export("overlay.wav", format="wav")
fast.export("fast.wav", format="wav")
combineWhole.export("combineWhole.wav", format="wav")
combineHalf.export("combineHalf.wav", format="wav")
combineQuarter.export("combineQuarter.wav", format="wav")
combineEigth.export("combineEigth.wav", format="wav")

