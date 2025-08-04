from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()


class Reddit_Scrape:
    def __init__(self):
        """ah"""
        self.headers = {"User-Agent": "python:subreddit.fetcher:v1.0 (by u/yourusername)"}
        self.mainpage = os.getenv("URL")

    def top_post(self, post):
        """ah"""
        response = requests.get(url=self.mainpage, headers=self.headers)
        data = response.json()
        if data["data"]["children"][post]["data"]["selftext"] == "":
            pass
        else:
            # print(data["data"]["children"][x]["data"]["selftext"])
            # print(data["data"]["children"][x]["data"]["url"])
            diction = {post:
                        {
                            data["data"]["children"][post]["data"]["title"]:
                            (data["data"]["children"][post]["data"]["selftext"],
                            f'https://www.reddit.com{data["data"]["children"][post]["data"]["permalink"]}.json')
                        }
                    }
            self.comments_url = diction[post][list(diction[post].keys())[0]][1] # print(list(post[1].keys())[0]) #dict_keys(['key string']) to just 'key string'
            return diction
    def top_comments(self):
        """ah"""
        try:
            data = requests.get(url=self.comments_url, headers=self.headers).json()

            for _ in range(3): #3 comments
                print(f"COMMENT {_ + 1}")
                print(data[1]['data']['children'][_]['data']['score'])
                print(data[1]['data']['children'][_]['data']['body'])
                #return something
        except:
            pass

scrape = Reddit_Scrape()
print(scrape)
post = scrape.top_post(3)
scrape.top_comments()
# print(list(post[1].keys())[0]) #dict_keys(['key string']) to just 'key string'
