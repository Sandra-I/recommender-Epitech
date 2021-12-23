import io
from google_api.Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload
import pandas as pd

class GetFileFromGoogleDrive:
    CLIENT_SECRET_FILE = 'google_api/client_secret_GoogleCloud.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    file_ids = ['1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ', '1WM9kvmlOhzuyepk77R7k0UM2-PAngkQ0', '1J1zoy6uPfCciaQH0WLMhMeC-b3SDV80m', '1PAy6z1PHJMCaAmWGmQXqf25epPAdplgn', '1UP8JwG0v9Nv6nUAYfc4kowbHeJ861lA0']

    # Ordre des ids correspondant à l'ordre des noms ci-dessous
    # file_names = ['clean_dataset.csv', 'best_item_by_cli.csv', 'frequence_item.csv', 'paired_item.csv', 'cli_article_rfm_segment.csv']

    clean_dataset = pd.DataFrame()
    best_item_by_cli_df = pd.DataFrame()
    frequence_item_df = pd.DataFrame()
    paired_item_df = pd.DataFrame()
    cli_article_rfm_segment = pd.DataFrame()

    def __init__(self):
        for file_id in self.file_ids:
            request = self.service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print('Download file {0}'.format(status.progress() * 100))

            fh.seek(0)

            if file_id == '1YzBXfLqRCm5yAs48mgmPIemhlUaV0jNJ':
                self.clean_dataset = pd.read_csv(fh, parse_dates=True)

            elif file_id == '1WM9kvmlOhzuyepk77R7k0UM2-PAngkQ0':
                self.best_item_by_cli_df = pd.read_csv(fh, parse_dates=True)

            elif file_id == '1J1zoy6uPfCciaQH0WLMhMeC-b3SDV80m':
                self.frequence_item_df = pd.read_csv(fh, parse_dates=True)

            elif file_id == '1PAy6z1PHJMCaAmWGmQXqf25epPAdplgn':
                self.paired_item_df = pd.read_csv(fh, parse_dates=True)

            elif file_id == '1UP8JwG0v9Nv6nUAYfc4kowbHeJ861lA0':
                self.cli_article_rfm_segment = pd.read_csv(fh, parse_dates=True)

        print('Downloading end')

    def get_clean_dataframe(self):
        return self.clean_dataset
    
    def get_best_item_by_cli_dataframe(self):
        return self.best_item_by_cli_df

    def get_frequence_item_dataframe(self):
        return self.frequence_item_df
    
    def get_paired_item_dataframe(self):
        return self.paired_item_df

    def get_rfm_cli_article_dataframe(self):
        return self.cli_article_rfm_segment
