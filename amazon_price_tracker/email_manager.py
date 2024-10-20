import smtplib

class EmailManager:
    def __init__(self):
        self.my_email = "your_email"
        self.password = "your_password"
        self.adrs_email = "addr_email"

    def send_email(self, sub, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email,password=self.password)

            msg = message
            from_ = self.my_email
            to_ = self.adrs_email
            subject = sub

            fmt = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}'

            connection.sendmail(from_, to_, fmt.format(from_, to_, subject, msg).encode('utf-8'))