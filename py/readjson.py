# coding = utf-8
import json
import os

num = 0
para = 0

for para in range(3):
    num = 0

    while num != 100:
        print("readjson" + str(para) + '-' + str(num))
        if os.path.isfile('./json/' + str(para) + '-' + str(num) + '.json'):
            f = open('./json/' + str(para) + '-' + str(num) + '.json', 'r', encoding='utf-8')
            content = eval(f.read())
            strContent = json.dumps(content, sort_keys=True, ensure_ascii=False, indent=2)
            newAllJson = {}
            jsonContent = json.loads(strContent)
            for i in range(len(jsonContent)):
                Id = jsonContent[i]['id']  # jsonContent[i]['Jname']#将id值作为键名
                del jsonContent[i]['id']
                if Id:
                    newAllJson[Id] = jsonContent[i]


            def toJson(content):
                return json.dumps(content, sort_keys=True, ensure_ascii=False, indent=2)


           


            

            fout = open('./fineJson/' + str(para) + '-' + str(num) + '.json', 'w', encoding='utf-8')
            newAllJson=str(newAllJson).replace("'",'"')
            fout.write(str(newAllJson))
        num += 1
