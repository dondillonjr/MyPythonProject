## Retrieve Random Joke from Internet

from urllib import request
import json

url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
#NOTE response below=200, which means you can read response
#makes request to pull jokes from internet api
print(r.getcode())

#shows list containing json payload (setup/puchline)
#print(r.read())

## reads joke response from api internet call
data = r.read()
#show joke response
print(data)
print()
## loads json document
jsonData = json.loads(data)
print(jsonData)
print()

for joke in jsonData:
    print(joke)
print()
print()
for joke in jsonData:
    print(f"SETUP= {joke['setup']}          JOKE= {joke['punchline']}")
print()
print()
for joke in jsonData:
    setup = joke["setup"]
    pline = joke["punchline"]
    print(f"Setup= {setup}     Joke= {pline}")