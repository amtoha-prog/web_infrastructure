from datetime import datetime, timezone
import requests


# Settings

SUBREDDIT = "AmItheAsshole"
HEADERS = {"User-Agent": "pythone:amitheasshole-info:v0.1 (by /u/Phone_Log9164)"}

def get_data(url):
  response = requests.get(url, headers=HEADERS, timeout=10)
  print("Status Code:", response.status_code)
  return response.json()


