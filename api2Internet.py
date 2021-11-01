## Retrieve Random Joke from Internet

from urllib import request
import json

url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
#NOTE response below=200, which means you can read response
#makes request to pull jokes from internet api
#print(r.getcode())

## reads joke response from api internet call
data = r.read()
#show joke response
#print(data)
#print()
## loads json document
jsonData = json.loads(data)
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