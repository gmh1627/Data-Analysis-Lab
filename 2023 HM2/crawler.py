# -*-coding: GBK -*-

# ������վ�������ԣ�������������վ��ȡ����200���γ̵���ϸ��Ϣ����¼�� json ��ʽ���ļ���
from bs4 import BeautifulSoup
import requests
import json
from multiprocessing.dummy import Pool
import time

# ��ȡ�γ���ҳ���ı��ĺ���
def crawl(url):
    # �����Ӧ
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    r = requests.get(url, headers=headers)
    html = r.content.decode('utf-8', 'ignore')

    my_page = BeautifulSoup(html, 'lxml')
    # lecΪ���浱ǰ�γ̶���������Ϣ���ֵ�
    lec = {}
    # ��ȡ��һ���������
    lec["�γ�����"] = my_page.find('span', class_='blue h3').get_text()
    # ��ȡ�ڶ����������
    rank1 = my_page.find(
        'ul', class_='text-muted list-inline list-unstyled ud-pd-sm').get_text()
    for itr in rank1.split('\n'):
        if len(itr):
            lec[itr.split('��')[0]] = itr.split('��')[1]
    # ��ȡ�������������
    rank2 = my_page.find(
        'table', class_='table table-condensed no-border').get_text()
    for itr in rank2.split('\n'):
        if len(itr):
            lec[itr.split('��')[0].lstrip()] = itr.split('��')[1]
    #���ؿγ̶����ֵ�
    return lec

# ��ȡ����ҳ�����пγ���ҳ���Ӳ�����crawl������ȡ�γ���Ϣ
# �����ر�����ȡ�Ŀγ���Ϣ��ɵ��б�
def get_url(url):
    # �����Ӧ
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
    r = requests.get(url, headers=headers)
    html = r.content.decode('utf-8', 'ignore')

    my_page = BeautifulSoup(html, 'lxml')
    # url_listΪ��ȡ�Ŀγ���ҳurl��ɵ�list
    url_list = []
    # ѭ����ȡ���пγ����Ӳ�����γ���ҳ��ȡ��Ϣ
    for tag in my_page.find_all('a', class_='px16'):
        url_new = tag.get('href')
        url_list.append('https://icourse.club/'+url_new)
    # ����10���̳߳�
    pool = Pool(10)
    # ����map���̳߳��е������̡߳�ͬʱ��ִ��crawl����
    return pool.map(crawl, url_list)
     
# �����������ڷ�ҳֱ���γ�������200
# pageΪҳ��,lec_listΪ���пγ���ɵ��б�
if __name__ == '__main__':
    #��ʼ��ʱ
    start_time = time.time()
    page = 1
    lec_list=[]
    while (len(lec_list) <= 200):
        lec_list += get_url('https://icourse.club/course/?page=%d' % page)
        page += 1
    #ת��Ϊjson��ʽ�����浽Ŀ���ļ�
    with open('pksq.json','w',encoding="utf-8")as f:
        json.dump(lec_list,f,ensure_ascii=False)
    #�����������ʱ��
    end_time = time.time()    
    run_time = end_time - start_time    
    print(run_time)
