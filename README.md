# Gmail automation

**Introduction**

In this project we will make an automated email sender. On given time and date it will send an email to perticular person. In addition to this we will be doing automation of other things as well using crontab scheduler.

**Requirement**

Linux, Python and pip >=2.7

**Steps:**
1. Setup gmail api [here](https://console.developers.google.com/ "Google Api")
2. Download clientid.json file
3. create new python file and copy below code
```python
import httplib2
import os
import oauth2client
from oauth2client import client, tools
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors, discovery

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'Gmail API Python Send Email'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-email-send.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    message1 = CreateMessage(sender, to, subject, msgHtml, msgPlain)
    SendMessageInternal(service, "me", message1)

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print 'Message Id: %s' % message['id']
        return message
    except errors.HttpError, error:
        print 'An error occurred: %s' % error

def CreateMessage(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string())}

def main():

    to = "###########@gmail.com"
    sender = "me"
    subject = "write any subject"
    msgHtml = "Hi<br/><br/>Cheers"
    msgPlain = "Hi\nPlain Email"
    SendMessage(sender, to, subject, msgHtml, msgPlain)

if __name__ == '__main__':
    main()
```
replace ```###########@gmail.com``` with any email

**Note:** clientid.json file and above file must be in same directory.


4. Open terminal 
```
crontab -e
```
 select appropriate editor (vim or nano).
 
 5. now you can schedule your email
 ```minute hour dayOfMonth month dayOfWeek command```
 
 Eg ```0 0 1 1 * python api_gmail.py``` this will send email on 1st of January at 12 AM.
 
 
 
