from email.message import EmailMessage
import smtplib

class EmailServer:

    def __init__(self):
        self.email_sender = 'tpttruong61030803@gmail.com'
        self.email_password = 'tsafeiolqnmaqmns'

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.email_sender, self.email_password)

    def send_email_jobs(self, email_receiver, id_jobs):

        subject = "New jobs for you"
        message = ''
        main_link = 'http://localhost:5173/mainjob/'    
        for id in id_jobs:
            message += f'{main_link}{id}\n'

        text = f'Subject: {subject}\n\n{message}'

        self.server.sendmail(self.email_sender, email_receiver, text)

    def close_server(self):
        self.server.close()