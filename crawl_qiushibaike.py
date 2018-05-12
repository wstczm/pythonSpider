import urllib2
from bs4 import BeautifulSoup

page = 1
url = "https://www.qiushibaike.com/8hr/page/%s/" % page
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
headers = {"User-Agent": user_agent}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
html = response.read()
bs = BeautifulSoup(html, "lxml")
items = bs.select("div.article.block.untagged.mb15")
idx = 1
for item in items:
    name = item.select("div.author.clearfix h2")[0].get_text().replace('\n', '').replace('\r', '').replace('\t', '')
    content = item.select("div.content span")[0].get_text().replace('\n', '').replace('\r', '').replace('\t', '')
    print "%s. %s : %s \n" % (idx, name, content)
    idx = idx + 1
