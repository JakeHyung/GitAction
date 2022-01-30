import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%BD%94%EB%A1%9C%EB%82%98&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=45&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1")
soup = bs(res.text,"lxml")
title = soup.select("a.news_tit")
titleList = []
for i in title :
    titleList.append(i.text)
dic = {"기사" : titleList}
df = pd.DataFrame(dic)
df.to_csv("data.csv",encoding="euc-kr",index=False)
