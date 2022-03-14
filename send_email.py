# Sends email
import smtplib,ssl
from dotenv import load_dotenv
load_dotenv()
import os
import certifi

sender = os.environ.get('EMAIL_USERNAME')
password = os.environ.get('EMAIL_PASSWORD')
server = 'smtp.transip.email'
port = 465

receive = 'hello@nielsveen.com'
def send_email(receiver,address,txid):
    message = f"""\
        Subject: You will receive 1 CRO

        You will receive 1 CRO on your address: {address}
        \n
        Keep track of the transaction here: {txid}
        """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    context = ssl._create_unverified_context()
    print('starting to send')
    with smtplib.SMTP_SSL(server,port,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,message)
        print('send email')

send_email(receive,'your address','your txid')

