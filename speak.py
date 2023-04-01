
# Import the google text to speech api and ability to open files
from gtts import gTTS
import os

# Our language choices
mytext = 'Hello world. It is nice to meet you.'
language = 'en'
accent = 'com'

# send the options to the server
myobj = gTTS(text=mytext, lang=language, slow=False, tld=accent)
  
# save a file for playing
myobj.save("welcome.mp3")
  
# Playing the saved file
os.system("open welcome.mp3")