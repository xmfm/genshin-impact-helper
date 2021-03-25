import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json


def send_ding(content, preurl, key):
    headers={'Content-Type': 'application/json'}
    msg = {
        'msgtype': 'text',
        'text': {'content': content}
    }
    timestamp = round(time.time() * 1000)  #时间戳
    presign = f'{timestamp}\n{key}'  #处理前的签名
    hmac_code = hmac.new(key.encode(), presign.encode(), digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote(base64.b64encode(hmac_code))
    url = preurl + f'&timestamp={timestamp}&sign={sign}'
    result = requests.post(url, data=json.dumps(msg), headers=headers)
    logging.info(time.strftime('%Y.%m.%d %H:%M:%S'), result.json().get('errmsg', 'error'))
