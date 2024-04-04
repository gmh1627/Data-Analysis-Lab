import re

def extract_paper_info2(papers_content):
    final_result = []
    # 使用正则表达式找到所有在 "<>" 之外的字符串
    for j in range(len(papers_content)):
        outside_brackets = re.split(r'<[^>]*>', papers_content[j])
        print(outside_brackets)
        # 遍历提取到的内容，删除含有'http'的字符串及其前面的字符串
        for i in range(len(outside_brackets)):
            if 'http' in outside_brackets[i]:
                flag = i
        final_result.append([])
        for i in range(flag + 1 , len(outside_brackets)):
            if outside_brackets[i]:
                final_result[j].append(outside_brackets[i])
    return final_result

# 测试这个函数
papers_content = ['<p>Some text <>http://example.com<> and more text</p>' , 'itemscope itemtype="http://schema.org/PublicationVolume"<span itemprop="volumeNumber">abs/2008.04552</span></span></a> (<span itemprop="datePublished">']
extracted_info = extract_paper_info2(papers_content)
print(extracted_info)