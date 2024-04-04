import re
import json

with open('page.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义一个列表来存储 Track 信息
tracks = []

# 定义正则表达式
track_pattern = re.compile(r'<h2 id=".*?">(.*?)</h2>')
author_pattern = re.compile(r'<span itemprop="name" title=".*?">(.*?)</span>')
title_pattern = re.compile(r'<span class="title" itemprop="name">(.*?)</span>')
page_pattern = re.compile(r'<span itemprop="pagination">(.*?)-(.*?)</span>')

# 找到 "Research Track Full Papers" 和 "Applied Data Science Track Full Papers" 的位置
start1 = content.find('Research Track Full Papers') - 50
start2 = content.find('Applied Data Track Full Papers') - 50
start3 = content.find('Hands On Tutorials') - 1

# 从整篇文本中划分出前两个Track中所有相邻"<cite"和"</cite>"之间的内容(即一篇文章的范围)
research_papers_content = re.split('<cite', content[start1:start2])[1:]
applied_papers_content = re.split('<cite', content[start2:start3])[1:]

def extract_paper_info(papers_content):
    papers = []
    for paper_content in papers_content:
        paper_content = re.split('</cite>', paper_content)[0]
        papers.append(paper_content)
    return papers
        
spit_research_content = extract_paper_info(research_papers_content)
spit_applied_content = extract_paper_info(applied_papers_content)

print("Number of research papers: ", len(research_papers_content))
print("Number of applied papers: ", len(applied_papers_content))

# 提取每篇paper的author、title和startPage, endPage
def extract_paper_info(papers_content):
    papers = []
    for paper_content in papers_content:
        authors = author_pattern.findall(paper_content)
        titles = title_pattern.findall(paper_content)
        pages = page_pattern.search(paper_content)
        startPage, endPage = pages.groups()
        papers.extend([{'authors': authors, 'title': title , 'startPage': startPage , 'endPage': endPage} for title in titles])
    return papers

# 提取 "Research Track Full Papers" 的论文信息
research_track = track_pattern.search(content[start1:start2]).group(1)
research_papers = extract_paper_info(spit_research_content)

# 提取 "Applied Data Science Track Full Papers" 的论文信息
applied_track = track_pattern.search(content[start2:start3]).group(1)
#applied_papers = extract_paper_info(spit_applied_content)
applied_papers = extract_paper_info(spit_applied_content)
# 将论文信息存储到字典列表中
tracks.append({'track': research_track, 'papers': research_papers})
tracks.append({'track': applied_track, 'papers': applied_papers})

# 将字典列表转换为 JSON 并写入文件
with open('kdd23.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f, indent=2)