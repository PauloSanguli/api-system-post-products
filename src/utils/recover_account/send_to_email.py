from email.message import EmailMessage
import smtplib



class sendEmail:
    
    def __init__(self, email: str, pwd_email: str):
        self.emailSystem = email
        self.pwdEmail = pwd_email


    def configureMSG(self,cod: int, email_user: str):
        self.msg = EmailMessage()
        self.cod = cod
        self.emailUser = email_user
        MSG = f"Cod: {self.cod}"

        self.msg['Subject'] = 'Cod to recover account'
        self.msg['From'] = self.emailSystem
        self.msg['To'] = self.emailUser
        self.msg.set_content(MSG)

    def SendMSG(self):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email, self.pwdEmail)
                smtp.send_message(self.msg)
        except:
            return {
                "msg": "message dont sended",
                "status": False
            }
        else:
            return {
                "msg": "message sended to the email",
                "status": True
            }

    