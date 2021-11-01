## Retrieve Page from Internet

from urllib import request

r = request.urlopen("http://www.google.com")
#NOTE response below=200, which means you can read response
print("\n")
print(r.getcode())
print("\n")
print(r.read())