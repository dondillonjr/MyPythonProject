## Retrieve Random Joke from Internet

import requests
import json

url = "http://official-joke-api.appspot.com/random_ten"
response = requests.get(url)
print(response.status_code)
jsonData = json.loads(response.text)
print(jsonData)
print()

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) ->str:
        return f"Setup= {self.setup}  Punchline= {self.punchline}"

jokes = []
for j in jsonData:
    joke = Joke( j["setup"], j["punchline"] )
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)