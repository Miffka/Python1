import requests

r = ""
url = "https://stepic.org/media/attachments/course67/3.6.2/324.txt"
r = requests.get(url)
nlines = len(r.text.splitlines())
print(nlines)
