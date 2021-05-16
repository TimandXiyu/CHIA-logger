import os
import sqlite3
import requests
from win32crypt import CryptUnprotectData

def getcookiefromchrome(host='.oschina.net'):
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()
        cookies={name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        print(cookies)
        return cookies


getcookiefromchrome('www.hpool.com')

# url='http://my.oschina.net/'
#
# httphead={'User-Agent':'Safari/537.36',}
#
# #设置allow_redirects为真，访问http://my.oschina.net/ 可以跟随跳转到个人空间
# r=requests.get(url,headers=httphead,cookies=getcookiefromchrome('.oschina.net'),allow_redirects=1)
# print(r.text)

