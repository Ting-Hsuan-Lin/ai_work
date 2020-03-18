import urllib.request as req
import json
url="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=bdc841eb-e8c8-41ee-abfc-1e198a96e905"
with req.urlopen(url) as res:
    data=json.load(res)
centerList=data["result"]["results"]
for centerName in centerList:
    print(centerName["ORG_NAME"],centerName["ADDRESS"])


