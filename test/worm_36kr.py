# -*- coding: utf-8 -*-
import re
import sys
import time

import pymysql
from bs4 import BeautifulSoup as BS
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf8')


URL = "http://36kr.com"
browser = webdriver.PhantomJS()
browser.get("http://36kr.com/")

def get_selist(url):
    try:
        soup = BS(browser.page_source, "html.parser")  # 解析网页
        arts = soup.findAll("div", {"class": re.compile(r'am-cf inner_li$')})  # 找到所有我要的<a>标签  得到一个list  接下来提取元素的href

        return arts  # 返回链接的list
    except Exception as e:  # 网页访问错误就返回空列表
        print(e)


def get_art_content(url):
    try:
        browser.get(url)
        soup = BS(browser.page_source, "html.parser")
        title = soup.find('div', {'class': 'mobile_article'}).h1.string
        keywords = ""
        words = soup.find_all('a', {'class': 'kr-tag-gray'})
        for word in words:
            keywords += word.string + " "
        if keywords != "":
            keywords = keywords[:-1]
        else:
            keywords = 'None'

        author = soup.find('span', {'class': 'name'}).string
        summary = soup.find('section', {'class': 'summary'}).string
        # content = (soup.find('section', {'class': 'textblock'})).replace('data-src','src')
        content = soup.find('section', {'class': 'textblock'})
        source = soup.find_all('section', {'class': 'article-footer-label'})[0]

        while (source.div):
            source = source.div
        if (source.string):
            source = 'copied'
        else:
            source = 'original'
        copySite = URL
        copyURL = url
        addedBy = author
        editor = author
        times = soup.find('abbr', {'class': 'time'}).string
        if times[-2] == '钟':
            times = time.time() - int(times[:-3]) * 60
        elif times[-2] == '时':
            times = time.time() - (int(times[:-3]) * 3600)
        else:
            times = time.time() - (int(times[:-2]) * 3600 * 24)

        timeArray = time.localtime(times)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        addedDate = otherStyleTime
        editedDate = addedDate
        return title, keywords, summary, content, source, copySite, copyURL, author, addedBy, editor, addedDate, editedDate
    except Exception as e:
        print(e)

def insert_db(arts):
    db = pymysql.connect("101.132.39.195", "dev", "Aa111111", "dandantuan")
    # db = pymysql.connect("112.74.185.158", "dev", "Aa111111", "dandantuan")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    for art in arts:
        # SQL 插入语句
        sql = "INSERT INTO eps_article(title,titleColor,alias, keywords, summary, content,source,copySite,copyURL,author,addedBy,editor,addedDate,editedDate ,`status`,`type`,submission,views,sticky,stickTime,stickBold,`order`,link,css,js,onlyBody,lang) VALUES ('%s','%s', '%s','%s','%s','%s','%s','%s', '%s','%s','%s','%s','%s','%s', '%s', '%s','%s','%d','%d','%s','%d', '%d','%s','%s','%s','%d','%s')" % (
        art["title"], art["titleColor"], art["alias"], art["keywords"], art["summary"], art["content"], art["source"],
        art["copySite"], art["copyURL"],
        art["author"], art["addedBy"], art["editor"], art["addedDate"], art["editedDate"], art["status"], art["type"],
        art["submission"], art["views"],
        art["sticky"], art["stickTime"], art["stickBold"], art["order"], art["link"], art["css"], art["js"],
        art["onlyBody"], art["lang"])
        print(sql)

        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()

    # 关闭数据库连接
    db.close()


result = []
arts = get_selist(URL)
for a in enumerate(arts):
    art = {}
    art_url = a[1].findAll(name="a", attrs={"href": re.compile(r'/.*?.html')})
    try:
        art_url = URL + art_url[0].attrs['href']
        title, keywords, summary, content, source, copySite, copyURL, author, addedBy, editor, addedDate, editedDate = get_art_content(
            art_url)
        art["title"] = title
        art["titleColor"] = ''
        art["alias"] = ''
        art["keywords"] = keywords
        art["summary"] = summary
        art["content"] = content
        art["source"] = source
        art["copySite"] = copySite
        art["copyURL"] = copyURL
        art["author"] = author
        art["addedBy"] = 'admin'
        art["editor"] = editor
        art["addedDate"] = addedDate
        art["editedDate"] = editedDate
        art["type"] = 'article'
        art["status"] = 'normal'
        art["submission"] = 0
        art["views"] = 0
        art["sticky"] = 0
        art["stickTime"] = addedDate
        art["stickBold"] = 0
        art["order"] = 0
        art["link"] = ''
        art["css"] = ''
        art["js"] = ''
        art["onlyBody"] = 0
        art["lang"] = 'zh-cn'
        result.append(art)
        print(art)
    except Exception as e:
        pass
insert_db(result)
