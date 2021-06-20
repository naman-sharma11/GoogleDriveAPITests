import io
import os.path
from prettytable import PrettyTable
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.dirname(dir_path)


class GoogleApiTest:
    def __init__(self):
        self.x = PrettyTable()
        self.x.field_names = ["S.No", "File Name", "File ID"]

        self.creds = None
        # Checking if token file is present
        if os.path.exists('{}/files/token.json'.format(dir_path)):
            self.creds = Credentials.from_authorized_user_file('{}/files/token.json'.format(dir_path), SCOPES)
        # Checking if credentials are valid, else creating new
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('{}/files/client_secret.json'.format(dir_path), SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('{}/files/token.json'.format(dir_path), 'w') as token:
                token.write(self.creds.to_json())
        # Creating service object of Google Drive API
        self.service = build('drive', 'v3', credentials=self.creds)

    def list_files(self):
        try:
            # Provides output list of maximum 1000 files
            results = self.service.files().list(pageSize=1000, fields="nextPageToken, files").execute()
            items = results.get('files', [])
            count = 1
            if not items:
                pass
            else:
                for item in items:
                    # Excluding folder mimetype from the results
                    if 'vnd.google-apps.folder' not in str(item):
                        self.x.add_row([count, item['name'], item['id']])
                        count += 1
            if count > 1:
                return True, self.x
            else:
                return False, None
        except Exception as exc:
            print("Exception in listing files {}".format(exc))
            return False, str(exc)

    def search_file(self, query):
        try:
            """ Searches for file based on query applicable on query term. 
            Google Drive Reference - https://developers.google.com/drive/api/v3/ref-search-terms?hl=en#file_properties
            """
            results = self.service.files().list(pageSize=1000, fields="nextPageToken, files(id, name)", q=query).execute()
            items = results.get('files', [])
            if not items:
                return None
            else:
                for item in items:
                    return item['id']
        except Exception as exc:
            print("Exception in search file {}".format(exc))
            return False

    def upload_file(self, file_name, file_path, mime_type):
        try:
            """ Uploades file to Google Drive irrespective of mimetype.
            Using resumable as True while uploading to support for large files.
            https://developers.google.com/drive/api/v3/manage-uploads?hl=en#resumable
            """
            metadata = {'name': file_name}
            media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
            file = self.service.files().create(body=metadata, media_body=media, fields='name').execute()
            search = self.search_file('name contains "{}"'.format(file.get('name')))
            if search is not None:
                return True
            else:
                return False
        except Exception as exc:
            print("Exception in upload file {}".format(exc))
            return False

    def download_files(self, file_id, target_file_name):
        try:
            # Downloads the file using the file id and takes input of file name with which downloaded file will be created.
            request = self.service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            with io.open(target_file_name, 'wb') as f:
                fh.seek(0)
                f.write(fh.read())
            if os.path.exists(target_file_name):
                return True
            else:
                return False
        except Exception as exc:
            print("Exception in download files {}".format(exc))
            return False

    def delete_file(self, file_id, file_name):
        try:
            # Deletes the file from Google Drive based on File ID. Also verifying file post deletion using search file.
            request = self.service.files().delete(fileId=file_id).execute()
            search = self.search_file('name contains "{}"'.format(file_name))
            if search is None:
                return True
            else:
                return False
        except Exception as exc:
            print("Exception in delete file {}".format(exc))
            return False
