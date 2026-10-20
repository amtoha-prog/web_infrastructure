from datetime import datetime, timezone
import requests


# Settings

SUBREDDIT = "AmItheAsshole"
HEADERS = {"User-Agent": "pythone:amitheasshole-info:v0.1 (by /u/Phone_Log9164)"}

# Function to get data from the Reddit API
def get_data(url):
  response = requests.get(url, headers=HEADERS, timeout=10)
  print("Status Code:", response.status_code)
  return response.json()


# Function to get subreddit information
def get_about(subreddit):
  data = get_data("https://www.reddit.com/r/" + subreddit + "/about.json")
  return data["data"]

# Function to get subreddit rules
def get_rules(subreddit):
  data = get_data("https://www.reddit.com/r/" + subreddit + "/about/rules.json")
  return data["rules"]

# Function to get the newest posts in a subreddit
def get_newest(subreddit):
  data = get_data("https://www.reddit.com/r/" + subreddit + "/new.json?limit=10")
  return data["data"]["children"]

# Main function to display subreddit information, rules, and newest posts
def main():
  about = get_about(SUBREDDIT)
  rules = get_rules(SUBREDDIT)
  newest = get_newest(SUBREDDIT)

  print("Subreddit name:", about["display_name"])
  print("Subreddit description:", about["description"])
  print("Number of subscribers:", about["subscribers"])

  print("\nRules:")
  for rule in rules:
    print("-", rule["short_name"])

  print("\n10 Newest posts:")
  for post in newest:
    print ("-", post["data"]["title"], "by", post["data"]["author"])


main()