import requests, json, sys
#_*_coding:utf-8 _*_

headers = {
    'X-Auth-Token': 'xxxxxxxxxxxxxxxxxxxxxx',
    'X-User-Id': 'xxxxxxxxxxxxxxxxxxxxxx',
    'Content-type': 'application/json'
}

subject = sys.argv[1]
message = sys.argv[2]

data = {
    "channel": "zabbix",
    "emoji": ":slight_frown:",
    "attachments":
        [{"color": "#ff2a00",
          "title": subject,
          "text": message}]
}
url = "https://rocketchat.rocketchat.com/api/v1/chat.postMessage"

r = requests.post(url=url, data=json.dumps(data), headers=headers)
print(r.json())
