# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

page = 1
url = "https://tieba.baidu.com/p/5644083341?pn=%s" % page
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
headers = {"User-Agent": user_agent}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html = response.read()
bs = BeautifulSoup(html, "lxml")
items = bs.select("div.l_post.l_post_bright.j_l_post.clearfix")

for item in items:
    name = item.select("div.d_author ul li.d_name a.p_author_name")[0].get_text(
    ).replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')

    try:
        content = item.select("div[id*='post_content_']")[0].get_text().replace('\n', '').replace('\r', '').replace('\t', '').replace('            ', '')
        tails = item.select("div.d_post_content_main div.core_reply.j_lzl_wrapper div.core_reply_tail.clearfix div.post-tail-wrap span")
        for tail in tails:
            if u'楼' in tail.get_text():
                idx = tail.get_text()
        print "%s - %s : %s \n" % (idx, name, content)
    except Exception as e:
        pass
