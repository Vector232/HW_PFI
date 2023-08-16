import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Messenger:
    #не особо понимаю, для чего это, ибо установить email не получилось
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        
    def send_message(self, subject, recipients, message):
        session = MIMEMultipart()
        session['From'] = self.login       
        session['To'] = ', '.join(recipients)
        session['Subject'] = subject
        session.attach(MIMEText(message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, session.as_string())

        ms.quit()


    def recieve_message(self):
        header = None

        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        _, data = mail.uid('search', None, criterion)

        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        mail.logout()

        return email_message


if __name__ == '__main__':
    # желательно через окружение
    login = 'login@gmail.com'
    password = 'qwerty'

    messenger = Messenger(login, password)


    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    messenger.send_message(subject, recipients, message)

    messenger.recieve_message()