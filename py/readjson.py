# coding = utf-8
import json
import csv
import os
num=0
para=0

for para in range(3):
	num=0
	print(para)
	while num!=100:
		print(num)
		if(os.path.isfile('../json/'+str(para)+'-'+str(num)+'.json')):
			f=open('../json/'+str(para)+'-'+str(num)+'.json','r',encoding='utf-8')
			content=eval(f.read())
			if (num==2 and para==25):
				print(content)
			strContent=json.dumps(content,sort_keys=True,ensure_ascii=False,indent=2)
			newAllJson={}
			jsonContent=json.loads(strContent)
			for i in range(len(jsonContent)):
					Id=jsonContent[i]['id']#jsonContent[i]['Jname']#将id值作为键名
					del jsonContent[i]['id']
					if Id:
						newAllJson[Id]=jsonContent[i]
			def toJson(content):
				return json.dumps(content,sort_keys=True,ensure_ascii=False,indent=2)
			tongs=[-1 for i in range(2000)]
			def tong(json):
				for i in newAllJson:
					tongs[int(i)]=0
					idx=i
			tong(newAllJson)
			fout=open('../fineJson/'+str(para)+'-'+str(num)+'.json','w',encoding='utf-8')
			fout.write('{\n')
			rs=[]
			for i in range(len(tongs)):
				if tongs[i]==0 :
					rs.append(i)
			for j in range(len(rs)):
				fout.write('"'+str(rs[j])+'":')
				if j!=len(rs)-1:
					fout.write(toJson(newAllJson[str(rs[j])])+',\n')
				else:
					fout.write(toJson(newAllJson[str(rs[j])])+'\n')
			fout.write('}')
		num+=1

