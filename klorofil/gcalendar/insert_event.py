
# Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def ginsert(title, dateTime):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.abspath('gcalendar/credentials.json'), SCOPES)
            creds = flow.run_local_server()
        # # Save the credentials for the next run
        # with open('token.pickle', 'wb') as token:
        #     pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    event = {
      'summary': title,
      'start': {
        'dateTime': dateTime,
        'timeZone': 'Asia/Kolkata',
      },
      'end': {
        'dateTime': dateTime,
        'timeZone': 'Asia/Kolkata',
      },
      'attendees': [
        {'email': 'tfreshup2@gmail.com'},
        {'email': 'sbrin@example.com'},
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=30, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return None
    gevents = []
    print ("Events:"+str(len(events)))
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        gevents.append([event['summary'], start, event['id']])
        print(start, event['summary'])
    return gevents
