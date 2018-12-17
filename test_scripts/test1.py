import pyttsx3

primary_engine = pyttsx3.init()

#Default configuration
primary_engine.setProperty("voice", "english")
primary_engine.setProperty("rate", 150)

primary_engine.say("This is a quick test")
primary_engine.runAndWait()

orig_rate = primary_engine.getProperty("rate")
orig_volume = primary_engine.getProperty("volume")
orig_voice = primary_engine.getProperty("voice")

#Start of the calibration
primary_engine.say("Calibration will now commence. Please select a fitting rate")
primary_engine.say("Do you want to hear the differences in rates?")
primary_engine.runAndWait()
rate_YON = input("Do you want to hear the differences in rates? [Y / N]: ")

if rate_YON == "Y":
    newVoiceRate = 50
    while newVoiceRate <= 200:
        print("Current rate:" + str(newVoiceRate))
        primary_engine.setProperty('rate', newVoiceRate)
        primary_engine.say("This is a rate test with rate " + str(newVoiceRate))
        primary_engine.runAndWait()
        newVoiceRate = newVoiceRate + 20
elif rate_YON == "N":
    pass
else:
    while rate_YON != "N" and rate_YON != "Y":
        print(rate_YON)
        print(type(rate_YON))
        primary_engine.say("Please type an appropriate answer")
        primary_engine.runAndWait()
        rate_YON = input("Please type an appropriate answer [Y / N]: ")
    if rate_YON == "Y":
        newVoiceRate = 50
        while newVoiceRate <= 200:
            print("Current rate:" + str(newVoiceRate))
            primary_engine.setProperty('rate', newVoiceRate)
            primary_engine.say("This is a rate test with rate " + str(newVoiceRate))
            primary_engine.runAndWait()
            newVoiceRate = newVoiceRate + 20
    else:
        pass

primary_engine.setProperty("rate", 150)
primary_engine.say("Please type the desired rate")
primary_engine.runAndWait()

userRateChoice = input("Please type the desired rate: ")
primary_engine.setProperty("rate", userRateChoice)

primary_engine.say("The chosen rate is " + userRateChoice)
primary_engine.runAndWait()

#Voice Selection
primary_engine.say("The next calibration will be the language. The default language is English, but there are a few variants available.")
primary_engine.runAndWait()
