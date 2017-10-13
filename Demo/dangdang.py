import time
from bs4 import BeautifulSoup
import requests
import csv
import codecs

url = "http://search.dangdang.com/?key=python&act=input&show=big&page_index="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
fileName = 'dangdang_PythonBook.csv'

def parseContent(response):
    soup = BeautifulSoup(response, "lxml")
    books = soup.find_all('a',class_='pic')
    # 指定编码为 utf-8, 避免写 csv 文件出现中文乱码
    with codecs.open(fileName, 'a+' ,encoding='utf_8_sig') as f:
        filednames = ['书名', '页面地址', '图片地址']
        writer = csv.DictWriter(f,filednames)
        # writer.writeheader()

        for book in books:
            if len(list(book.children)[0].attrs) == 3:
                img = list(book.children)[0].attrs['data-original']
            else:
                img = list(book.children)[0].attrs['src']
            writer.writerow({filednames[0]: book.attrs['title'], filednames[1]: book.attrs['href'], filednames[2]: img})

index = 1 
while index <= 2:
    request = requests.get(url=url+str(index), headers=headers)
    print('第' + str(index) + "页")
    index = index + 1
    parseContent(request.text)
    time.sleep(1)
