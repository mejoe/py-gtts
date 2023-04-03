
# Import the google text to speech api and ability to open files
from gtts import gTTS
import os, requests, json

# get the joke
jokesite = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = json.loads(jokesite.text)

# Store the joke in a variable
mytext = joke["setup"] + joke["punchline"]

# send the options to the server and save
myobj = gTTS(text=mytext)
myobj.save("say.mp3")
  
# Playing the saved file
os.system("open say.mp3")





