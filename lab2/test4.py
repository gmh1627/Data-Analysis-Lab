import re

content = '''<cite class="data tts-content" itemprop="headline"><span itemprop="author" itemscope itemtype="http://schema.org/Person"><span class="this-person" itemprop="name">Florian Adriaens</span><img src="https://dblp.dagstuhl.de/img/orcid-mark.12x12.png" style="padding-left:0.25em;" alt="" title="0000-0001-7820-6883"></span>, <span itemprop="author" itemscope itemtype="http://schema.org/Person"><a href="https://dblp.dagstuhl.de/pid/269/4508.html" itemprop="url"><span itemprop="name" title="Honglian Wang">Honglian Wang</span></a><img src="https://dblp.dagstuhl.de/img/orcid-mark.12x12.png" style="padding-left:0.25em;" alt="" title="0009-0008-6463-392X"></span>, <span itemprop="author" itemscope itemtype="http://schema.org/Person"><a href="https://dblp.dagstuhl.de/pid/g/AristidesGionis.html" itemprop="url"><span itemprop="name" title="Aristides Gionis">Aristides Gionis</span></a><img src="https://dblp.dagstuhl.de/img/orcid-mark.12x12.png" style="padding-left:0.25em;" alt="" title="0000-0002-5211-112X"></span>:<br> <span class="title" itemprop="name">Minimizing Hitting Time between Disparate Groups with Shortcut Edges.</span> <a href="https://dblp.dagstuhl.de/db/conf/kdd/kdd2023.html#AdriaensWG23"><span itemprop="isPartOf" itemscope itemtype="http://schema.org/BookSeries"><span itemprop="name">KDD</span></span> <span itemprop="datePublished">2023</span></a>: <span itemprop="pagination">1-10</span></cite>'''

text_only = re.sub('<.*?>', '', content)
#print(text_only)

import re

paper_content = '<span itemprop="isPartOf" itemscope itemtype="http://schema.org/Periodical"><span itemprop="name">CoRR</span></span> <span itemprop="isPartOf" itemscope itemtype="http://schema.org/PublicationVolume"><span itemprop="volumeNumber">abs/2002.07076</span></span></a> (<span itemprop="datePublished">2020</span>)<meta property="genre" content="computer science"></li></ul></div></div><div class="hideable">'
year_pattern = re.compile(r'<span itemprop="datePublished">(.*?)</span>')

match = year_pattern.search(paper_content)
if match:
    year = match.group(1)
    print(year)  # 输出：2020