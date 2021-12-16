from Google import Create_Service

CLIENT_SECRET_FILE = 'google_api/client_secret_GoogleCloud.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

print('dir(service)')
print(dir(service))
