import wikitextparser as wtp
import json
import csv
# ~ parsed = wtp.parse("""{{任务表| type =远征| 编号 =D1| <!--401-->前置 =A5
# ~ | 日文任务名字 =はじめての「遠征」！| 日文任务说明 =艦隊を「遠征」に出発させよう！
# ~ | 中文任务名字 =初次的「远征」！| 中文任务说明 =舰队出发「远征」！
# ~ | 燃料 =30| 弹药 =30| 钢铁 =30| 铝 =30| 奖励 ={{家具箱（小）}}*1
# ~ | 备注 =任意远征1次}}""")
# ~ print(parsed.templates[0].pformat())
# ~ equitfile=open('./equip.txt',encoding='utf-8')
# ~ equit=equitfile.read()
# ~ equit=json.loads(equit)
# ~ print(len(equit))
# ~ print(equit)
# ~ for i in range(len(equit)):
	# ~ print(equit[i]['id'])
# ~ f=csv.reader(open('quests.csv','r',encoding='utf-8'))
# ~ for i in f:
	# ~ print(i)
# ~ dicts= {
    # ~ "Jname": "主力オブ主力、精強「十駆」出撃準備ヨシ！",
    # ~ "code": "A93",
    # ~ "desc": "第十驱逐舰队编队任务：将完全由改装甲型驱逐舰「夕云改二」「卷云改二」「风云改二」，以及「秋云改二」4艘舰船编队以组成的最为精锐强大的「第十驱逐队」(4艘编队)！ 第一舰队编成，夕云改二旗舰+卷云+风云+秋云 奖励:12.7cm連装砲D型改二 ★+2以下奖励二选一：高速修复材 ×6特制家具职人",
    # ~ "name": "主力中的主力，精锐强大的「十驱」出击准备完毕！"
  # ~ }
# ~ del dicts['Jname']
# ~ print(dicts)
try:
	test=open('./json.json')
except FileNotFoundError:
	print('没有找到文件')
