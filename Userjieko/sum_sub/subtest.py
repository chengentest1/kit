import requests
import json
base_url="http://127.0.0.1:5006"
def add_normal():
    url=base_url+"/add/?a=3&b=8"
    res=requests.get(url)
    print(type(res.json().get("result")))


def sub_normal():
    url=base_url+"/api/sub"

    headers={"Content_Type":"application/json"}
    data={"a":33,"b":12}
    data=json.dumps(data)
    res=requests.post(url,headers=headers,data=data)
    print(res)
    print(res.json().get("code"))
    print(res.json().get("msg"))
    print(res.json().get("result"))
if __name__=="__main__":
    add_normal()