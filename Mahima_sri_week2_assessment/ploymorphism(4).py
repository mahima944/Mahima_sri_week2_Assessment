
class Notification:
    def send(self, message):
        print(f"Sending notification: {message}")

class EmailNotification(Notification):
    def send(self, message):  
        print(f"Sending Email: {message}")


class SMSNotification(Notification):
    def send(self, message):  
        print(f"Sending SMS: {message}")


email = EmailNotification()
email.send("Hello via Email!")  

sms = SMSNotification()
sms.send("Hello via SMS!")  
