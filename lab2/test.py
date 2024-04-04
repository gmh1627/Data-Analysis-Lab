import re
import requests
import json
import time
import random

# 打开并读取 "page.txt" 文件
with open('page.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义正则表达式
author_link_pattern = re.compile(r'<span itemprop="author" itemscope itemtype="http://schema.org/Person"><a href="(.*?)" itemprop="url">')
orcID_pattern = re.compile(r'<img alt="" src="https://dblp.dagstuhl.de/img/orcid.dark.16x16.png" class="icon">(.{19})</a></li>')
researcher_pattern = re.compile(r'<head><meta charset="UTF-8"><title>dblp: (.*?)</title>')
year_pattern = re.compile(r'<span itemprop="datePublished">(.*?)</span>')

# 找到 "Research Track Full Papers" 和 "Applied Data Track Full Papers" 的位置
start1 = content.find('Research Track Full Papers')
start2 = content.find('Applied Data Track Full Papers')
end = len(content)

# 提取这两个部分的内容，并找到前 10 个 "persistent URL:" 之间的内容
research_papers_content = content[start1:start2].split('<cite')[1:11]
applied_papers_content = content[start2:end].split('<cite')[1:11]

def extract_paper_info(papers_content):
    papers = []
    for paper_content in papers_content:
        paper_content = re.split('</cite>', paper_content)[0]
        papers.append(paper_content)
    return papers
        
spit_research_content = extract_paper_info(research_papers_content)
spit_applied_content = extract_paper_info(applied_papers_content)

def extract_paper_info2(paper_content):
    final_result = []
    # 使用正则表达式找到所有在 "<>" 之外的字符串
    outside_brackets = re.split(r'<[^>]*>', paper_content)
    # 遍历提取到的内容，删除含有'http'的字符串及其前面的字符串
    flag = -1
    for i in range(len(outside_brackets)):
        if 'http' in outside_brackets[i]:
            flag = i
    for i in range(flag + 1 , len(outside_brackets)):
        if outside_brackets[i]:
            final_result.append(outside_brackets[i])
    return final_result

# 定义一个列表来存储研究者信息
researchers = []

# 访问每篇文章里所有作者的链接，获取作者的 orcID 和论文信息
for papers in [research_papers_content, applied_papers_content]:
    for paper in papers:
        author_links = author_link_pattern.findall(paper)
        for link in author_links:
            link_content = requests.get(link)
            response = link_content.text
            
            #爬虫时频繁请求服务器，可能会被网站认定为攻击行为并报错"ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接"，故采取以下两个措施
            #使用完后关闭响应
            link_content.close()  
            # 在各个请求之间添加随机延时等待
            time.sleep(random.randint(1, 3))
            
            researcher = researcher_pattern.search(response).group(1)
            orcID = orcID_pattern.findall(response)
            
            # 找到 "<li class="underline" title="jump to the 2020s">" 和 "<li class="underline" title="jump to the 2010s">" 之间的内容
            start = response.find('2020 &#8211; today')
            end = response.find('<header id="the2010s" class="hide-head h2">')
            # 提取这部分的内容，并找到所有 "</cite>" 之间的内容
            papers_content = response[start:end].split('</cite>')[0:-1]
            
            papers_dict = []
            
            for paper_content in papers_content:
                spit_content = extract_paper_info2(paper_content)
                year = int(year_pattern.search(paper_content).group(1))
                authors = []
                publishInfo = []
                for i in range(0 , len(spit_content) - 1):
                    if spit_content[i] != ", " and (spit_content[i+1] == ", " or spit_content[i+1] == ":"):
                        authors.append(spit_content[i])
                    elif spit_content[i][-1] == '.':
                        title = spit_content[i]
                        for k in range(i+2 , len(spit_content)):
                            publishInfo.append(spit_content[k])
                # 创建一个新的字典来存储每篇文章的信息
                paper_dict = {'authors': authors, 'title': title, 'publishInfo': ''.join(publishInfo), 'year': year}
                papers_dict.append(paper_dict)
            researchers.append({'researcher': researcher, 'orcID': orcID, 'papers': papers_dict})

# 将字典列表转换为 JSON 并写入 "researchers.json" 文件
with open('researchers.json', 'w', encoding='utf-8') as f:
    json.dump(researchers, f, indent=2)