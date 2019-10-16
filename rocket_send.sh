#!/usr/bin/env bash
/usr/bin/curl -s \
-H "X-Auth-Token: xxxxxxxxxxxxxxxxxxxxxx" \
-H "X-User-Id: xxxxxxxxxxxxxxxxxxxxxx" \
-H "Content-type: application/json"  \
https://rocketchat.rocketchat.com/api/v1/chat.postMessage  \
-d '{ "channel": "#zabbix", "text": "$1\n$2" }'
echo