# coding:utf-8
import requests
import re
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'ffwdsite'))
from ffwdsite.settings import redis_conn
# import sendmail


class App(object):
    r9 = redis_conn(db=9)
    # r9 = redis.Redis(host='127.0.0.1', port=6379, db=9, password='123')

    def __init__(self, key):
        self.key = key
        self.url = "http://www.51cto.com/recommnews/%s.htm" % key
        # self.url = "https://www.v2ex.com"
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'}

    def get_html(self):
        # html = self.session.get(self.url, headers=self.headers, timeout=20)
        html = requests.get(self.url, headers=self.headers, timeout=20)
        print html.status_code
        html = html.content.decode("gb2312", "ignore").encode("utf-8", "replace")
        lists = re.findall('''<div class="list-li">(.*?)<span class="share">''', html, re.S)
        return lists

    def get_data(self):
        try:
            lists = self.get_html()
            if len(lists) > 0: 
                self.r9.delete(self.key)
                for data in lists:
                    img = re.findall('<img src="(.*?)">', data)[0]
                    url, title = re.findall('<a href="(.*?)" target.*>(.*?)</a>', data)[0]
                    info = re.findall('<p class="info">(.*?)</p>', data, re.S)[0]
                    date = re.findall('<div class="time">(.*)', data)[0].strip()
                    self.r9.rpush(self.key, (img, url, title, info, date))

        except Exception as e:
            print e
 #          sendmail.send_mail(['747553934@qq.com'], "51cto_new None", "51cto news get lists = [] %s" % e)


if __name__ == '__main__':
    # r9 = redis.Redis(host='127.0.0.1', port=6379, db=9)
    App("list1").get_data()
    App("list2").get_data()
    App("list3").get_data()
    App("list4").get_data()
