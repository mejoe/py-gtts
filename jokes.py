import requests
import json


data = requests.get("https://official-joke-api.appspot.com/random_joke")
a = json.loads(data.text)

print(a["setup"])
print(a["punchline"])
