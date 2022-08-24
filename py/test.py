import re

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
# ~ try:
# ~ test=open('./json.json')
# ~ except FileNotFoundError:
# ~ print('没有找到文件')
# ~ equipUrl='http://kcwikizh.github.io/kcdata/slotitem/all.json'
# ~ headers = {
# ~ 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
# ~ 'cookie':"_ga=GA1.2.1881705690.1629543107; VEE=wikitext; vector-nav-p-.E5.B8.B8.E7.94.A8.E9.80.9F.E6.9F.A5=true; vector-nav-p-.E5.87.BA.E5.87.BB.E6.B5.B7.E5.9F.9F=true; vector-nav-p-tb=true; vector-nav-p-.E5.8F.82.E4.B8.8E.E7.BC.96.E5.86.99kcwiki=true; vector-nav-p-.E6.B2.99.E7.9B.92=true; vector-nav-p-.E6.B8.B8.E6.88.8F.E6.96.87.E5.8C.96=true; vector-nav-p-kcwiki.E6.97.97.E4.B8.8B.E9.A1.B9.E7.9B.AE=true; vector-nav-p-.E9.81.93.E5.85.B7=true; vector-nav-p-.E5.85.A5.E6.B8.A0.E3.83.BB.E8.A1.A5.E7.BB.99=true; vector-nav-p-.E6.94.B9.E8.A3.85.E3.83.BB.E5.B7.A5.E5.8E.82=true; kcwiki_UserName=Callofblood; kcwiki_UserID=5277; kcwiki_Token=a696414057db9b77a8a4472b77eeaf90; _gid=GA1.2.1109110936.1631275946; kcwiki__session=1tin18vua2u0c4nmk9i511h50fbbsqm7; vector-nav-p-.E4.BB.BB.E5.8A.A1=true"
# ~ }
# ~ r = requests.get(equipUrl, headers=headers)    
# ~ file=open('./equip.txt','w+',encoding='utf-8')#写入网页内所有内容
# ~ file.write(str(r.text))
# ~ print(r.text)
test = """
{{任务表| type =出击| 编号 = 2103B4|<!--909--> 前置 =2103B2
| 日文任务名字 =【桃の節句：拡張作戦】春の攻勢作戦！
| 日文任务说明 =「桃の節句作戦」精鋭艦隊の編成、北方海域北方AL海域、西方海域カレー洋リランカ島沖、中部北海域ピーコック島沖へ展開、各海域の敵戦力を痛打、これを撃滅せよ！
| 中文任务名字 =「桃之节句：扩张作战」！春季攻势作战！
| 中文任务说明 =「桃之节句作战」编成精锐舰队，出击「[[3-5|北方阿留申海域]]」(3-5)「[[4-5|咖喱洋里兰卡岛海域]]」（4-5)「[[6-4|中部北海域孔雀岛近海]]」(6-4)，将各海域敌战力痛打击灭！
| 燃料 =880| 弹药 =880| 钢铁 =880| 铝 =880| 奖励 ='''{{菱饼}}×4'''<br/>以下奖励五选一：'''<br/>[[文件:KanMusu335Banner.jpg|link=松轮]]<br/>[[文件:KanMusu339Banner.jpg|link=佐渡]]<br/>[[文件:KanMusu340Banner.jpg|link=对马]]<br/>[[文件:KanMusu365Banner.jpg|link=福江]]<br/>[[文件:KanMusu370HDBanner.png|link=平户|160px]]'''
| 备注 ='''周常任务'''<br/>分别出击3-5、4-5、6-4并取得S胜。}}"""
# ~ test="""{{任务表| type =编制| 编号 =A1|<!--101-->|前置 =
# ~ | 日文任务名字 =はじめての「編成」！| 日文任务说明 =2隻以上の艦で編成される「艦隊」を編成せよ！
# ~ | 中文任务名字 =初次的「编成」！| 中文任务说明 =以两艘以上的阵容编成「舰队」！
# ~ | 燃料 =20| 弹药 =20| 钢铁 =0| 铝 =0| 奖励 =[[文件:KanMusu012Banner.jpg|link=白雪]]
# ~ | 备注 =}}"""
patternLink = re.compile(r'文件:(\w){1,20}.(\w){1,20}\|link=')  # 处理wikilink格式
pattern = re.compile('文件:\w{10,20}.[j|p][p|n]g\|link=')  # 处理wikilink格式
link = pattern.findall(test)
print(link)
