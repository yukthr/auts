# This script helps in deleting some files from Gdrive as more images are uploaded from security system!

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
import re

SCOPES = 'https://www.googleapis.com/auth/drive'

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('/Users/rmadupu/Desktop/credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

results = service.files().list(
    pageSize=100, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])

files_to_delete = []
files_to_delete_names = []

if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        ps = re.compile(r'^(\d)')
        if ps.findall(item['name']):
            files_to_delete.append(item['id'])
            files_to_delete_names.append(item['name'])
            print(u'{0} ({1})'.format(item['name'], item['id']))


def delete_file(service, file_id):
    try:
        for i in files_to_delete:
            service.files().delete(fileId=i).execute()
            print("file {} deleted succesfully!".format(i))
    except:
        print("Error Found")

for i in files_to_delete:
    delete_file(service,i)

