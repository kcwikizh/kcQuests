import json
import os
import re

import requests
import wikitextparser as wtp


def getValue(arr):
    arr = arr.replace("}}", ' ')  # 处理wiki格式
    arr = arr.replace('"', '')
    arr = arr.replace('‘', '')
    arr = arr.replace('’', '')
    arr = arr.replace("'", '')
    arr = arr.replace("{", '')
    arr = arr.replace("}", '')
    arr = arr.replace("[[", '')
    arr = arr.replace("]]", '')

    arr = arr.replace("１", '1')  # 处理日文数字
    arr = arr.replace("２", '2')
    arr = arr.replace("３", '3')
    arr = arr.replace("４", '4')
    arr = arr.replace("５", '5')
    arr = arr.replace("６", '6')
    arr = arr.replace("７", '7')
    arr = arr.replace("８", '8')
    arr = arr.replace("９", '9')
    arr = arr.replace("０", '0')
    arr = arr.replace('（', '(')  # 处理括号
    arr = arr.replace('）', ')')

    arr = arr.replace("red", "")  # 处理wiki标签
    arr = arr.replace("Red", "")
    arr = arr.replace('green', '')
    arr = arr.replace('Green', '')

    patternh5 = re.compile('<.+?>')  # 处理h5标签
    h5 = patternh5.findall(arr)

    for i in range(len(h5)):
        arr = arr.replace(h5[i], '')

    flag = 0
    for i in range(len(arr)):
        if arr[i] == '=' and flag == 0:  # 获取'='后的字符串
            idx = i
            flag = 1
            return arr[idx + 1:].strip()
    return ''


def filterMap(desc):
    patternPre = re.compile('([「]?\d-\d)\|(.*?)\((\d-\d)\)')
    res = patternPre.findall(desc)
    for i in res:
        tmp = i[0] + '|' + i[1]
        desc = desc.replace(tmp, '')
        tmp2 = '(' + i[2] + ')'
        desc = desc.replace(tmp2, i[2] + ' ')
    return desc


num = 0
equipUrl = 'http://kcwikizh.github.io/kcdata/slotitem/all.json'  # 读取装备数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    # ~ 'cookie':"_ga=GA1.2.1881705690.1629543107; VEE=wikitext; vector-nav-p-.E5.B8.B8.E7.94.A8.E9.80.9F.E6.9F.A5=true; vector-nav-p-.E5.87.BA.E5.87.BB.E6.B5.B7.E5.9F.9F=true; vector-nav-p-tb=true; vector-nav-p-.E5.8F.82.E4.B8.8E.E7.BC.96.E5.86.99kcwiki=true; vector-nav-p-.E6.B2.99.E7.9B.92=true; vector-nav-p-.E6.B8.B8.E6.88.8F.E6.96.87.E5.8C.96=true; vector-nav-p-kcwiki.E6.97.97.E4.B8.8B.E9.A1.B9.E7.9B.AE=true; vector-nav-p-.E9.81.93.E5.85.B7=true; vector-nav-p-.E5.85.A5.E6.B8.A0.E3.83.BB.E8.A1.A5.E7.BB.99=true; vector-nav-p-.E6.94.B9.E8.A3.85.E3.83.BB.E5.B7.A5.E5.8E.82=true; kcwiki_UserName=Callofblood; kcwiki_UserID=5277; kcwiki_Token=a696414057db9b77a8a4472b77eeaf90; _gid=GA1.2.1109110936.1631275946; kcwiki__session=1tin18vua2u0c4nmk9i511h50fbbsqm7; vector-nav-p-.E4.BB.BB.E5.8A.A1=true"
}
r = requests.get(equipUrl, headers=headers)
file = open('./equip.txt', 'w+', encoding='utf-8')
file.write(str(r.text))
equitfile = open('./equip.txt', encoding='utf-8')
equit = equitfile.read()
equit = json.loads(equit)
exception_string = {'|★': '★'}


def bonusTrim(bonus):
    patternBonus = re.compile('\s*[\*|×]\s*')
    rs = patternBonus.findall(bonus)
    for i in rs:
        bonus = bonus.replace(i, '*  ')
    # ~ print(bonus)
    return bonus


for para in range(3):
    print(para)
    num = 0
    while num != 100:
        if (os.path.isfile('./rs/' + str(para) + '-' + str(num) + '.txt')):
            file = open('./rs/' + str(para) + '-' + str(num) + '.txt', 'r+', encoding='utf-8')
            tasks = file.readlines()
            l = len(tasks)
            temp = ''
            wikiContents = []
            for i in range(l):
                if ('{{任务表' in tasks[i]):
                    wikiContents.append(temp)
                    temp = ''
                    start = i
                temp += tasks[i]
            wikiContents.append(temp)
            dicts = []
            for i in range(len(wikiContents)):
                patternWiki = re.compile(r'{{(.+?)}}')  # 处理装备卡
                wiki = patternWiki.findall(wikiContents[i])
                for j in wiki:
                    if '|' in j:
                        # ~ print(j)
                        left = j.split('|')[0]
                        right = j.split('|')[1]
                        patternNum = re.compile('编号(.+?)(\d+)')
                        Num = re.match(patternNum, right)
                        if Num:
                            for k in range(len(equit)):
                                if (equit[k]['id'] == int(Num.group(2))):
                                    wikiContents[i] = wikiContents[i].replace(j, equit[k]['name'])
                patternLink = re.compile('文件:\w{10,20}.[j|p][p|n]g\|link=')  # 处理wikilink格式
                link = patternLink.findall(wikiContents[i])

                if link:
                    for l in link:
                        wikiContents[i] = wikiContents[i].replace(l, ' ')
                for string in exception_string.keys():
                    if string in wikiContents[i]:
                        wikiContents[i] = wikiContents[i].replace(string, exception_string[string])
                parsed = wtp.parse(wikiContents[i])
                if (len(parsed.templates) > 0):
                    content = parsed.templates[0].pformat()
                    content = content.split('\n')
                    patternId = re.compile('<!--(.+?)-->')
                    patternPre = re.compile('^[A-Za-z0-9]{1,10}$')
                    pre = []
                    taskId = ""
                    code = ""
                    name = ""
                    taskId = ""
                    desc = ""
                    nowbonus = ""
                    memo = ""
                    for i in content:
                        Id = patternId.findall(i)
                        if (len(Id) > 0):
                            taskId = Id[0]
                        if ('编号' in i):
                            code = getValue(i)
                            code = code.replace('<!--', '')
                            print(code)
                        if ('中文任务名字' in i):
                            name = getValue(i)
                        if ('|<!--' in i):
                            print(i)
                        if ('中文任务说明' in i):
                            desc = getValue(i)
                            print(desc)
                            desc = filterMap(desc)
                        if ('奖励' in i):
                            tempbonus = getValue(i)
                            if (tempbonus):
                                nowbonus = "奖励:" + tempbonus

                        if ('备注' in i):
                            memo = getValue(i)
                            memo = filterMap(memo)
                        if ('前置' in i):
                            # print(i)
                            p = getValue(i)
                            p = p.replace('<!--', '')
                            p = patternPre.findall(p)
                            if (len(p) > 0):
                                pre.append(p[0])
                        if ('覆盖' in i):
                            cover = getValue(i)
                    temp = {
                        "code": code,
                        "name": name,
                        "id": taskId,
                        "desc": desc,
                        "memo": nowbonus,
                        "memo2": memo,
                        "pre": pre,
                        "cover": "cover"
                    }
                    # ~ if(num==1 and para==1):
                    # ~ print('this is temp:'+str(temp))
                    taskId = ''
                    dicts.append(temp)
                    code = ""
                    name = ""
                    taskId = ""
                    desc = ""
                    nowbonus = ""
                    memo = ""
                    cover = ""
                    pre = []
            wfile = open('./json/' + str(para) + '-' + str(num) + '.json', 'w+', encoding='utf-8')
            wfile.write('[')
            for i in range(len(dicts)):
                if i != len(dicts) - 1:
                    wfile.write(str(dicts[i]) + '\n,')  # 写入
                else:
                    wfile.write(str(dicts[i]) + '\n')
            wfile.write(']')
            wfile.close()
            print(para)
            rfile = open('./json/' + str(para) + '-' + str(num) + '.json', 'r+', encoding='utf-8')
            rcontent = rfile.read()
            rcontent = rcontent.replace("'", '"')  # 将所有的'转换为"
            wfile = open('./json/' + str(para) + '-' + str(num) + '.json', 'w+', encoding='utf-8')
            wfile.write(rcontent)
        num += 1
# ~ 编号--code
# ~ 中文任务名字--name
# ~ 中文任务说明--desc
# ~ 奖励--bonus
# ~ 备注--memo
