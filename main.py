from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
#make sure to include url=
headers = {"User-Agent": "python:subreddit.fetcher:v1.0 (by u/yourusername)"}
url = os.getenv("URL")
url2 = os.getenv("URL2")

response = requests.get(url=url, headers=headers)
response2 = requests.get(url=url2, headers=headers)
data = response.json()
data2 = response2.json()

for x in range(10): #top 10 posts
    print(data2["data"]["children"][x]["data"]["title"])



# print(data)
subreddit = data[0]['data']['children'][0]['data']['subreddit'] #subreddit name
print(subreddit)
print(data[0]['data']['children'][0]['data']['title']) #post title
print(data[0]['data']['children'][0]['data']['selftext']) #post text
for _ in range(3): #3 comments
    print(f"COMMENT {_}")
    print(data[1]['data']['children'][_]['data']['score'])
    print(data[1]['data']['children'][_]['data']['body'])