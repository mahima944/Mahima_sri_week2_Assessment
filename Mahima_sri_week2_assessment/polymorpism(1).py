class Logger:
    def log(self, message, level="info"):
        if level.lower()== "error":
            print(f"[ERROR]:{message}")
        elif level.lower()=="warning":
            print(f"[warning]:{message}")
        else:
            print(f"[info]: {message}")
            
logger=Logger()
logger.log("system started")
logger.log("Low disk space", "warming")
logger.log("File not found", "error")
        