#导入所需要的库
from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
 
for i in range(1,10) :    #需要补充"?"完善从第几页到第几页
    n = 0
    list_url = []
    url = 'https://？'+str(i)+'.html'#需要补充"?"完善
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
     
    req = requests.get(url=url, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html')  #这里的‘html’很关键，不同的网页有不同的选项
    
    img_url = bf.find_all("a") #这里的‘？’关键，是图片网址对应的大类或字典名称
    # img_url = img_url.prettify() 
    
    #print(bf.prettify())
    # print(img_url)
    # aa='aa'
    # print(type(aa)=='calss str')
    #获取图片链接
    for each in img_url:
        list_url.append(each.get('data-original'))#这里的‘？’关键，是图片的网址对应的直接变量名称
     
    #创建文件
    if not os.path.exists('./imgs'):
        os.mkdir('./imgs')
     
    #用循环将图片链接转化为图片
    while n < (len(list_url)):
        if type(list_url[n]) == str :
            img_url = list_url[n]
            urlretrieve(img_url, './imgs/%s.jpg' % (n+i*1000))   #文件命名？
        n = n + 1
 
print("下载完成")