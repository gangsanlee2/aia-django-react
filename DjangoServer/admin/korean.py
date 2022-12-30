import os.path

from konlpy.tag import Okt

from admin.path import dir_path

okt = Okt()
okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
with open(os.path.join(dir_path('samsung_report'), 'data', 'kr-Report_2018.txt'),'r',
          encoding='UTF-8') as f:
    texts = f.read()
print(texts)
