import speech_recognition as sr 
audioFile = ("sample.wav") # only converts audio present in .wav extention
r = sr.Recognizer()

with sr.AudioFile(audioFile) as source:
    audioFile = r.record(source)

try:
    print(r.recognize_google(audioFile))
except sr.UnknownValueError:
    print("Google couldn't recognize audio") # except is a type of error
except sr.RequestError:
    print("Check audio file once")
    
