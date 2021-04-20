from api_client import ApiClient
import json


api = ApiClient()

query_params = {'page_no': 1, "page_size": 2}
rooms_resp = api.request("GET", "http://127.0.0.1:5000/rooms", query_params=query_params, _preload_content=True)
data = json.loads(rooms_resp.data)

f1 = "D:/work/py-apps/client/config/openapi.json"

with open(f1) as f:
    oas_data = json.load(f)


urls = []

"""
path:
method: 
parameters,
order: 
dependent: [""]
type: full|incremental
pagination: true or false
"""
for path, path_dict in oas_data.get("paths"):

    for method, method_dict in path_dict:
        url = {"path": path, "method": method, "parameters": method_dict["parameters"]}

"""
* get list of paths
* iterate in order
* get parameters static and dynamic 
"""

