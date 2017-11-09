
from __future__ import print_function

import subprocess
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

from apiclient import errors

def DeleteMessage(service, user_id, msg_id):
    try:
        service.users().messages().delete(userId=user_id, id=msg_id).execute()
        print("Message with id: deleted successfully.")
    except errors.HttpError, error:
        print("An error occurred:")
        print(error)

if __name__ == "__main__":
    SCOPES = 'https://mail.google.com/'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

    threads = GMAIL.users().threads().list(userId='me', q='is:unread after:2017/04/25').execute().get('threads', [])
    # print(threads)
    count = 0
    # threadd = GMAIL.users().messages().modify(userId='me', id=message_id,body={ 'removeLabelIds': ['UNREAD']}).execute()
    # GET https://www.googleapis.com/gmail/v1/users/me/messages?q="in:sent after:2017/04/19 before:2017/04/21")
    for thread in threads:
        tdata = GMAIL.users().threads().get(userId='me', id=thread['id']).execute()
        nmsgs = len(tdata['messages'])
        if nmsgs > 0:
            msg = tdata['messages'][0]['payload']
            subject = ''
            for header in msg['headers']:
                if header['name'] == 'Subject':
                    subject = header['value']
                    break
            if subject:
                count = count + 1
                print(subject)
                if subject == 'light1_on':
                    print('Done')
                    for sn in threads:
                        if sn['snippet'] == 'Smart-City':
                            print(sn['snippet'])
                            print(sn['id'])
                            print(sn)
                            DeleteMessage(GMAIL,'me',sn['id'])
                        break
                break
