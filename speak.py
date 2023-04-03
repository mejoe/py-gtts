# Import the google text to speech api and ability to open files
from gtts import gTTS
import os

# what do we want to say?
mytext = 'Jimena is weirder than the word weird.'

# send the choices to the server and save
myobj = gTTS(text=mytext)
myobj.save("welcome.mp3")
  
# Play the saved file
os.system("open welcome.mp3")