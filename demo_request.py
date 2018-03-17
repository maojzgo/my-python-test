import requests
import json

data = {
    'name':'zhangsan',
    'age':'25'
}

url='https://www.zhihu.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
ret=requests.get(url,headers=headers)

# print(ret.url)
# print(type(ret))
# print(ret.cookies)
# print(type(ret.text))
#
# print(ret.content.decode('utf-8'))

ret.encoding='utf-8'

print(ret.text)
#print(json.loads(ret.text))