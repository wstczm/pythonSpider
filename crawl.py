import cookielib
import urllib2

url = "http://www.baidu.com"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}


cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

request = urllib2.Request(url, headers=headers)
try:
    # response = urllib2.urlopen(request)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print response.read()


