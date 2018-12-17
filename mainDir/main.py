import mainDir.log as log_Module
import flask
from flask import request
import datetime

##Flask setupcalls under here##
app = flask.Flask(__name__)

##Flask defenitions##
@app.route('/testDef', methods=['GET'])
def testDef():
    i = "The test is working"
    log_Module.logModule("API GET request return: " + i, logCreateDate, datetime.datetime.now())
    return "The test is working"

##Initial calls under here##

#Log setup
logCreateDate = datetime.datetime.now()
log_Module.logSetup(logCreateDate)

#Starting the API
app.run()