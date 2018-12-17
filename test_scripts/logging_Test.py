import mainDir.log as log_Module
import datetime
import time

logging_Createdate = datetime.datetime.now()

log_Module.logSetup(logging_Createdate)

log_Module.logModule("Yeah this is our first log entry :D", logging_Createdate, datetime.datetime.now())
time.sleep(2)
log_Module.logModule("Second log entry confirmed", logging_Createdate, datetime.datetime.now())