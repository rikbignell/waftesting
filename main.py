import requests

url = ""
http_proxy  = ""
https_proxy = ""
proxies = {
              "http"  : http_proxy,
              "https" : https_proxy
}
headers = {'Content-Type': 'application/json'}
with open('payloads.txt') as file:
    data = file.read().splitlines()

for payload in data:
    body = {'data': payload}
    r = requests.post(url, json=body, headers=headers, proxies=proxies)
    print ("Request: {}. Response code: {}".format(body, r.status_code))
