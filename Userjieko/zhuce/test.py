import requests
import json
base_url="http://127.0.0.1:5012"

def test_add_normal():
    url=base_url+"/api/user/reg/"

    headers={"Content_Type":"application/json"}
    data={"name":"lili","passwd":"123456"}
    data=json.dumps(data)
    res=requests.post(url,headers=headers,data=data)
    print(res)
    print(res.json().get("code"))
    print(res.json().get("msg"))
    print(res.json().get("data"))
if __name__=="__main__":
    test_add_normal()