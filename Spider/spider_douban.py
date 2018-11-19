import requests
from lxml import etree

URL = input('请输入URL：')
r = requests.get(URL)
print(r)

#通过URL传递http参数
# keyword = 'wd'
# keyword_value = input('请输入关键词:')
# playload = {keyword : keyword_value}
# r = requests.get(URL, params=playload)

