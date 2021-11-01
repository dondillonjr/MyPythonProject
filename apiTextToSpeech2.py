## Retrieve Random Joke from Internet

import requests
import pyttsx3
import json

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"Setup= {self.setup}  Punchline= {self.punchline}"

##################################################################
url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
jsonData = json.loads(response.text)
print(jsonData)
print()

jokes = []
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

for j in jsonData:
    joke = Joke(j["setup"], j["punchline"])
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")
pyttsx3.speak(f"We found {len(jokes)} jokes")

for the_joke in jokes:
    print(the_joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(the_joke.setup)
    pyttsx3.speak("The Punchline")
    pyttsx3.speak(the_joke.punchline)

pyttsx3.speak("That's all folks, please re-run to hear more jokes")