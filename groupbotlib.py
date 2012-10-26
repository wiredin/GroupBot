import smtplib

class groupbot:
 

    def __init__(self, name):
        print "Hello, I'm " + name

    def connectGmail(self, fromaddr, tooaddr, username, password):   
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.starttls()
        self.server.login(username,password)
        self.fromaddr= fromaddr
        self.tooaddr = tooaddr 

    def setMessage(self, msg):
        self.msg = msg

    def sendMessage(self):
        self.server.sendmail(self.fromaddr, self.tooaddr, self.msg)

    def disconnectGmail(self):
        self.server.quit()
  

