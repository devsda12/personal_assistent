import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Could not understand")
except sr.RequestError as e:
    print("Error; {0}".format(e))