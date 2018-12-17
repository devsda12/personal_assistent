import os
import datetime
import time

#Method that gets called for the initial log setup
def logSetup(origDate):

    #Begin check if logDir exists
    if os.path.isdir("Logs") is False:
        os.mkdir("Logs")

    #Create the datetime object (disabled because of getting date from main for better functionality)
    #origDate = datetime.datetime.now()

    #Make new logfile with start entry
    emptyFile = open("Logs/" + str(origDate)[0:19] + " Logfile", "w+")
    emptyFile.write("[" + str(origDate)[0:19] + "]" + " File initiated. Waiting for log input")
    emptyFile.close()


#Official method that gets called from main
def logModule(logData, origDate, curDate):

    #Opening the created logfile
    logFile = open("Logs/" + str(origDate)[0:19] + " Logfile", "a+")

    #Writing the data into the file
    logFile.write("\n[" + str(curDate)[0:19] + "]" + " " + logData)

    #Closing the file
    logFile.close()


"""
#Testrun the functions
createDate = datetime.datetime.now()
logSetup(createDate)
i = 0
while i < 100:
    logModule("This is testdata", createDate, datetime.datetime.now())
    i = i + 1
    time.sleep(0.1)
"""