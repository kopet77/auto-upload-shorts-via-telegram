ini adalah panduan Super Lengkap mulai dari VPS benar-benar kosong (baru beli/reset) hingga bot berjalan. Saya asumsikan kamu menggunakan OS standar VPS yaitu Ubuntu (20.04 atau 22.04 ke atas).

🟢 TAHAP 1: Persiapan di Laptop/PC (Wajib)
Karena VPS tidak punya browser, kamu HARUS membuat file token.json di Laptop dulu.

Siapkan Folder: Buat folder bot_veo di laptop.

Download Credential: Masuk Google Cloud Console -> Download client_secret.json -> Simpan di folder bot_veo.

Install Library: Buka CMD/Terminal di folder itu:

Bash

pip install google-auth-oauthlib google-auth-httplib2
Buat Script Auth (auth_local.py): Copy script ini, simpan sebagai auth_local.py di folder yang sama.

Python

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
Jalankan: python auth_local.py -> Login -> Simpan file token.json yang muncul.

🔵 TAHAP 2: Setup VPS (Dari Kosong)
Login ke VPS kamu menggunakan SSH (Putty atau Terminal).

1. Update System & Install Python Jalankan perintah ini satu per satu (copas saja):

Bash

# 1. Update daftar paket
sudo apt update && sudo apt upgrade -y

# 2. Install Python, PIP, dan Screen (untuk background process)
sudo apt install python3 python3-pip python3-venv screen -y

# 3. Cek apakah python sudah terinstall
python3 --version
# (Harusnya muncul Python 3.x.x)
2. Buat Folder Bot

Bash

# Buat folder
mkdir veobot
cd veobot

# Buat Virtual Environment (Agar library rapi & tidak konflik sistem)
python3 -m venv venv

# Aktifkan Virtual Environment
source venv/bin/activate
# (Tanda (venv) akan muncul di sebelah kiri terminal kamu)
🟡 TAHAP 3: Membuat File di VPS
Sekarang kita akan membuat 3 file kode langsung di dalam VPS.

2. Buat .env Ketik: nano .env Paste dan ISI DENGAN DATA KAMU:

Plaintext

TELEGRAM_TOKEN=123456:Ganti_Dengan_Token_Bot_Telegram
GOOGLE_API_KEY=AIzaSy_Ganti_Dengan_API_Key_Veo_Gemini
Tekan Ctrl+X, lalu Y, lalu Enter.


🟠 TAHAP 4: Upload Token & Install
Sekarang folder VPS veobot sudah punya 3 file. Kurang satu: token.json yang ada di laptop kamu.

1. Upload token.json

Cara Mudah: Buka file token.json di laptop (pakai Notepad), copy semua isinya.

Di VPS, ketik nano token.json.

Paste isinya.

Save (Ctrl+X, Y, Enter).

2. Install Library (Pastikan kamu masih di dalam venv, ada tanda (venv) di terminal)

Bash

pip install -r requirements.txt
🔴 TAHAP 5: Menjalankan Bot 24 Jam
Agar bot tidak mati saat SSH ditutup, gunakan screen.

Bash

# 1. Buka sesi screen baru
screen -S botkucing

# 2. Jalankan bot
python bot_final.py
Jika muncul tulisan 🤖 Bot Active, berarti sukses!

Cara Keluar dari VPS:

Tekan Ctrl + A, lepas, lalu tekan D (Ini akan "detach" screen, bot tetap jalan di background).

Ketik exit untuk log out dari VPS.

Cara Cek Bot Lagi: Login VPS -> Ketik screen -r botkucing.

Selesai! Coba chat bot kamu sekarang: /shorts A tiny kitten crying alone in a box under heavy rain

Bot akan:

Buat video AI Veo.

Pilih judul random: "Lonely 😿 #aiandcats...".

Upload ke Shorts kamu.
