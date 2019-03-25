import urllib.request

Resp = urllib.request.urlopen('https://google.com')
page = Resp.read()
Data = page.decode('utf-8')
print(Data)
#print(Resp.readline())
#print(Resp.read())



