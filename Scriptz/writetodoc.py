from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io
from io import BytesIO
from googleapiclient.http import MediaIoBaseDownload
def writedoc(id):
	with open('token.pickle', 'rb') as token:
        	    creds = pickle.load(token)
	service = build('drive', 'v3', credentials=creds)
	file_id = str(id)
	request = service.files().export_media(fileId=file_id,
	 mimeType='text/plain')
	fh = io.FileIO(id + '.txt', 'wb')
	downloader = MediaIoBaseDownload(fh, request)
	done = False
	while done is False:
	    status, done = downloader.next_chunk()
	    print("Download %d%%." % int(status.progress() * 100))
