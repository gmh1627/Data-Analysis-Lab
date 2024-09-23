# -*-coding: GBK -*-

# 利用网站遍历策略，从评课社区网站爬取至少200个课程的详细信息，记录于 json 格式的文件中
from bs4 import BeautifulSoup
import requests
import json
from multiprocessing.dummy import Pool
import time

# 爬取课程主页的文本的函数
def crawl(url):
    # 获得响应
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    r = requests.get(url, headers=headers)
    html = r.content.decode('utf-8', 'ignore')

    my_page = BeautifulSoup(html, 'lxml')
    # lec为保存当前课程对象所有信息的字典
    lec = {}
    # 获取第一个红框内容
    lec["课程名称"] = my_page.find('span', class_='blue h3').get_text()
    # 获取第二个红框内容
    rank1 = my_page.find(
        'ul', class_='text-muted list-inline list-unstyled ud-pd-sm').get_text()
    for itr in rank1.split('\n'):
        if len(itr):
            lec[itr.split('：')[0]] = itr.split('：')[1]
    # 获取第三个红框内容
    rank2 = my_page.find(
        'table', class_='table table-condensed no-border').get_text()
    for itr in rank2.split('\n'):
        if len(itr):
            lec[itr.split('：')[0].lstrip()] = itr.split('：')[1]
    #返回课程对象字典
    return lec

# 爬取主网页的所有课程主页链接并调用crawl函数爬取课程信息
# 并返回本次爬取的课程信息组成的列表
def get_url(url):
    # 获得响应
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    r = requests.get(url, headers=headers)
    html = r.content.decode('utf-8', 'ignore')

    my_page = BeautifulSoup(html, 'lxml')
    # url_list为爬取的课程主页url组成的list
    url_list = []
    # 循环爬取所有课程链接并进入课程网页爬取信息
    for tag in my_page.find_all('a', class_='px16'):
        url_new = tag.get('href')
        url_list.append('https://icourse.club/'+url_new)
    # 定义10个线程池
    pool = Pool(10)
    # 利用map让线程池中的所有线程‘同时’执行crawl函数
    return pool.map(crawl, url_list)
     
# 主函数，用于翻页直至课程数大于200
# page为页码,lec_list为所有课程组成的列表
if __name__ == '__main__':
    #开始计时
    start_time = time.time()
    page = 1
    lec_list=[]
    while (len(lec_list) <= 200):
        lec_list += get_url('https://icourse.club/course/?page=%d' % page)
        page += 1
    #转化为json格式并保存到目标文件
    with open('pksq.json','w',encoding="utf-8")as f:
        json.dump(lec_list,f,ensure_ascii=False)
    #计算程序运行时间
    end_time = time.time()    
    run_time = end_time - start_time    
    print(run_time)
