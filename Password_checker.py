import requests
import hashlib
def final(data,five5,tail3):
    new_=five5+tail3
    print(tail3)
    #print("this is fianl-",new_)
    hashes=[line.split(':') for line in data.splitlines()]
    for h,count in hashes:
        if h==tail3:
            print("password found!!!")
            print(h)
            print("password repeated:",count)
            break


def request_api(query_data,tail2):
    url="https://api.pwnedpasswords.com/range/"+query_data
    res=requests.get(url)
    final(res.text,query_data,tail2)

def passw(password):
    sha1pass=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    five,tail=sha1pass[:5],sha1pass[5:]
   # print(sha1pass)
    request_api(five,tail)



        
passw('password123')
 

