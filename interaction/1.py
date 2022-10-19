import requests as requests
import urllib3
from ping3 import ping


# http = urllib3.PoolManager()
# url = 'http://192.168.0.89/cm?cmnd=Status'
# resp = http.request('GET', url)
# # print(resp.status)
# try:
#     if resp.status == 200:
#         print('sensor online')
#         print(resp.data.decode('utf-8'))
# except TimeoutError:
#     print('sensor offline')

ip_sensor = '192.168.0.87'
if ping(ip_sensor, timeout=1):
    print('sensor online ping')
else:
    print('sensor offline ping')







# pprint(resp.data.decode('utf-8'))
#
#
# resp = http.request('HEAD', url)
# pprint(resp.headers['Content-Type'])
