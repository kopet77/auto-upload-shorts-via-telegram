import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

if not os.path.exists(CLIENT_SECRET_FILE):
    print("❌ File 'client_secret.json' tidak ada!")
    exit()

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
print("Login browser & PILIH CHANNEL YOUTUBE...")
creds = flow.run_local_server(port=0)

with open('token.json', 'wb') as token:
    pickle.dump(creds, token)
print("✅ token.json berhasil dibuat!")
