#задача 2 - переход по множеству ссылок

import requests

task2 = ""
url = "https://stepic.org/media/attachments/course67/3.6.3/699991.txt"
r = requests.get(url)
task2 = r.text

k = 0
while task2[:2] != "We":
    r = requests.get(url)
    task2 = r.text
    url = "https://stepic.org/media/attachments/course67/3.6.3/" + task2
    k += 1
    print(k)

print(task2)

with open("306_output2.txt", "w") as ouf:
    ouf.write(str(task2))