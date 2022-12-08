import json
import time
import websocket
import requests
import os
from keep_alive import keep_alive

def log(TOKEN):

    status = "online"

    headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
    print(headers)
    userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
    username = userinfo["username"]
    discriminator = userinfo["discriminator"]
    userid = userinfo["id"]

    def onliner(token, status):
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
        start = json.loads(ws.recv())
        heartbeat = start['d']['heartbeat_interval']
        auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
        ws.send(json.dumps(auth))
        online = {"op":1,"d":"None"}
        time.sleep(heartbeat / 1000)
        ws.send(json.dumps(online))

    def run_onliner():
      os.system("clear")
      print(f"Logged in as {username}#{discriminator} ({userid}).")
      while True:
        onliner(TOKEN, status)
        time.sleep(30)

    keep_alive()
    run_onliner()

while True:
    try:
        token = "NDQ5NjMxODQzMjE0Njg4MjY2.G3HJWb.w7Hhl55fudastjw8kpSRKWO2yAeiezrFWDFyf8"
        log(token)
    except:
        pass