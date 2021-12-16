import os
import io
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

import pandas as pd

CLIENT_SECRET_FILE = 'google_api/client_secret_GoogleCloud.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# file_ids = ['1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ', '1WM9kvmlOhzuyepk77R7k0UM2-PAngkQ0', '1J1zoy6uPfCciaQH0WLMhMeC-b3SDV80m', '1PAy6z1PHJMCaAmWGmQXqf25epPAdplgn', '1UP8JwG0v9Nv6nUAYfc4kowbHeJ861lA0']

# file_names = ['clean_dataset.csv', 'best_item_by_cli.csv', 'frequence_item.csv', 'paired_item.csv', 'cli_article_rfm_segment.csv']



file_ids = ['1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ']
file_names = ['clean_dataset.csv']

for file_id, file_name in zip(file_ids, file_names):
    # file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print('Download {0}'.format(status.progress() * 100))
        # print("Download %d%%." % int(status.progress() * 100)

    fh.seek(0)

    clean_dataset = fh
    df = pd.read_csv(clean_dataset, parse_dates=True)
    print(df.head())



# class GetFileFromGoogleDrive:
#     CLIENT_SECRET_FILE = 'google_api/client_secret_GoogleCloud.json'
#     API_NAME = 'drive'
#     API_VERSION = 'v3'
#     SCOPES = ['https://www.googleapis.com/auth/drive']

#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     file_ids = ['1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ']
#     file_names = ['clean_dataset.csv']

#     def __init__(self):
#         for file_id, file_name in zip(self.file_ids, self.file_names):
#             # file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
#             request = self.service.files().get_media(fileId=file_id)
#             fh = io.BytesIO()
#             downloader = MediaIoBaseDownload(fh, request)
#             done = False
#             while done is False:
#                 status, done = downloader.next_chunk()
#                 print('Download {0}'.format(status.progress() * 100))
#                 # print("Download %d%%." % int(status.progress() * 100)

#             fh.seek(0)

