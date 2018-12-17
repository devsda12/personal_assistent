import pyttsx3
import speech_recognition as sr


#Initialization function for the speech output
def initializeSpeech():
    primary_engine = pyttsx3.init()

    #Default configuration
    primary_engine.setProperty("voice", "english")
    primary_engine.setProperty("rate", 150)

    return primary_engine


#Initialization function for the speech listener
def initializeListener():
    r = sr.Recognizer()

    return r


#Ambient listener for the keyword
def ambientListener():
    #Starting with catching audio from microphone
    with sr.Microphone(device_index=4) as source:
        listener.adjust_for_ambient_noise(source)
        print("Listener online! Talk!")
        audio = listener.listen(source)

    #Try to recognize the speech in the audio
    try:
        data = listener.recognize_sphinx(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Could not understand")
        data = "Could not understand"

    return data


#Speak function to output the given string to speech
def speak(speakString):
    if isinstance(speakString, str):
        primary_engine.say(speakString)
        primary_engine.runAndWait()
    else:
        primary_engine.say("Error Code 1, the returned value is not a string, do you want me to give you the raw output?")
        primary_engine.runAndWait()


#Initial calls under here
primary_engine = initializeSpeech()
listener = initializeListener()

#Test calls under here
while True:
    data = ambientListener()
    speak(data)