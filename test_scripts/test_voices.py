import pyttsx3

engine = pyttsx3.init()

voices = ["default", "english", "english-north", "english_rp", "english_wmids", "english-us"]

engine.setProperty("rate", 150)

for voice in voices:
    print(voice)
    engine.setProperty("voice", voice)
    engine.say("Testing the voice, this is a quick test for the voice tester with a few modifications. Pronaunciations are tested and this should be an exclamation mark!")
    engine.runAndWait()

