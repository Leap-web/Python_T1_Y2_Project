class Logger:
    
    def log(self,sms=None,error_code=None,detail=None):
        if sms is not None :
            print(f"Log:{sms}")
        elif error_code is not None and detail is not None:
            print(f"Error Code:{error_code}, Details: {detail}")
        else:
            print("Unknown format")

logger = Logger()
logger.log("System started")
logger.log(error_code=404, detail =  {'url': '/not-found'})
logger.log()

