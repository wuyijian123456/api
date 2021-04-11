import requests
import pytest
def test_get_token():
    url='http://219.134.240.180:51103/api/oauth/connect/token'
    data={
        "username":'admin',
        "password":'1q2w3E*',
        "grant_type":'password',
        "client_id":'vue.client'
}
    res=requests.post(url=url,data=data)
    assert res.status_code==200,"用例断言错误"
    print(res.status_code)
    print(res.json())
    print(res.text)
    print(res.content)
    print(res.headers)