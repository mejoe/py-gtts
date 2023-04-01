
# Import the google text to speech api and ability to open files
from gtts import gTTS
import os
import requests
import json

# get the joke
data = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = json.loads(data.text)

#print(joke["setup"])
#print(joke["punchline"])



# Store the joke in a variable
mytext = joke["setup"] + " ... " + joke["punchline"]

# Set other options for speaking
language = 'en'
accent = 'com'

# send the options to the server
myobj = gTTS(text=mytext, lang=language, slow=False, tld=accent)
  
# save a file for playing
myobj.save("welcome.mp3")
  
# Playing the saved file
os.system("open welcome.mp3")





