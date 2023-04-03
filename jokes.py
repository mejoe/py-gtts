import requests, json

# get the joke
jokesite = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = json.loads(jokesite.text)

# print the joke
print(joke["setup"])
print(joke["punchline"])
