import time
import requests

url = "https://discord.com/api/v9/users/@me/settings"

with open("authorization.txt", "r") as file:
        key = file.read().strip()
File = open("text.txt", "r")
lines = File.readlines()

def ChangeStatus(message):

    header = {
        "authorization": key
    }

    jsonData = {
        "status": "online",
        "custom_status": {
            "text": message
        }
    }
    request = requests.patch(url, headers=header, json=jsonData)

while True:

    for line in lines:

        ChangeStatus(line.split("\n")[0])
        time.sleep(3)