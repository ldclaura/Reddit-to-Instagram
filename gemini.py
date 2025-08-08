import requests
import os
from dotenv import load_dotenv

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
load_dotenv() #do not forget this, os.getenv doesnt work if you dont have this.
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="""Could you please come up with a possible solution?:
    **insert results of redditscrape**"""
)
print(response.text) 
print(type(response.text))

with open("re.txt", "w") as f:
    f.write(response.text)

