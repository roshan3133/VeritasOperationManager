import logging
import time

date = time.strftime("%d-%m-%Y")
today = time.strftime("%d-%m-%Y-%H:%M")

# Logging ##########################
log = logging.getLogger(__name__)
#log = logging.getLogger()
log.setLevel(logging.INFO)

# create a file handler
logfile = "logs"+"_"+date 
handler = logging.FileHandler("logs/"+logfile)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(handler)
#return log
####################################
