import requests
import json,pytest
def test_recordlist():
    base_url = 'http://219.134.240.180:51103/api/aims/medicalRecord'
    url = base_url + '/medicalRecordList'
    data ={
        "StartTime":'2021-04-03',
        "EndTime": '2021-04-10',
        "DeptCode":'',
        "pageIndex":1 ,
        "pageSize":1
    }
    res = requests.get(url,params=data)
    res_d=json.loads(res.text)
    print(res.url)
    print(type(res.text))
    print(res.status_code)
    print(json.loads(res.text))
    assert res_d['data'][0]['name']=='谢怡湘'

