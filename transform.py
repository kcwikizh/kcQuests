import wikitextparser as wtp
import re
import json
import os
def getValue(arr):
	arr=arr.replace("}}",' ')
	arr=arr.replace('"','')
	arr=arr.replace('‘','')
	arr=arr.replace('’','')
	arr=arr.replace("'",'')
	arr=arr.replace("{",'')
	arr=arr.replace("}",'')
	arr=arr.replace("[[",'')
	arr=arr.replace("]]",'')
	arr=arr.replace("}",'')
	
	
	arr=arr.replace("１",'1')
	arr=arr.replace("２",'2')
	arr=arr.replace("３",'3')
	arr=arr.replace("４",'4')
	arr=arr.replace("５",'5')
	arr=arr.replace("６",'6')
	arr=arr.replace("７",'7')
	arr=arr.replace("８",'8')
	arr=arr.replace("９",'9')
	arr=arr.replace("０",'0')
	patternh5=re.compile('<.+?>')
	h5=patternh5.findall(arr)

	for i in range(len(h5)):
		arr=arr.replace(h5[i],'')
	
	# ~ print(arr)
	flag=0
	for i in range(len(arr)):
		if arr[i]=='=' and flag==0:
			idx=i
			flag=1
			
			return arr[idx+1:].strip()
	return ''
num=0

equitfile=open('./equip.txt',encoding='utf-8')
equit=equitfile.read()
equit=json.loads(equit)





for para in range(3):
	# ~ print(para)
	num=0
	while num!=100:
		if(os.path.isfile('./rs/'+str(para)+'-'+str(num)+'.txt')):
			file=open('./rs/'+str(para)+'-'+str(num)+'.txt','r+',encoding='utf-8')
			tasks=file.readlines()
			l=len(tasks)
			temp=''
			wikiContents=[]
			for i in range(l):
				if('{{任务表' in tasks[i]):
					wikiContents.append(temp)
					temp=''
					start=i
				temp+=tasks[i]
			wikiContents.append(temp)
			dicts=[]
			for i in range(len(wikiContents)):
				patternWiki=re.compile(r'{{(.+?)}}')
				wiki=patternWiki.findall(wikiContents[i])
				for j in wiki:
					if '|' in j:
						# ~ print(j)
						left=j.split('|')[0]
						right=j.split('|')[1]
						patternNum=re.compile('编号(.+?)(\d+)')
						Num=re.match(patternNum,right)
						if Num:
							for k in range(len(equit)):	
								if (equit[k]['id']==int(Num.group(2))):
									# ~ print(equit[k]['name'])#将编号换成名字
									wikiContents[i]=wikiContents[i].replace(j,equit[k]['name'])
				patternLink=re.compile(r'文件:(\w){1,20}.(\w){1,20}\|link=')
				link=patternLink.search(wikiContents[i])
				if link:
					wikiContents[i]=wikiContents[i].replace(link.group(),'')
				parsed = wtp.parse(wikiContents[i])
				if(len(parsed.templates)>0):
					content=parsed.templates[0].pformat()
					content=content.split('\n')
					patternId=re.compile('<!--(.+?)-->')			
					for i in content:
						Id=patternId.findall(i)
						if (len(Id)>0):
							taskId=Id[0]
						if ('编号' in i):
							code=getValue(i)
							code=code.replace('<!--','')
						if ('中文任务名字' in i):
							name=getValue(i)
						if('|<!--' in i):
							print(i)
						if ('中文任务说明' in i):
							desc=getValue(i)
						if ('奖励' in i):
							bonus=getValue(i)
						if ('备注' in i):
							memo=getValue(i)
					temp={
						"code":code,
						"name":name,
						"id":taskId,
						"desc":desc+' '+memo+' 奖励:'+bonus,
					}
					taskId=''
					dicts.append(temp)
			wfile=open('./json/'+str(para)+'-'+str(num)+'.json','w+',encoding='utf-8')
			wfile.write('[')	
			for i in range(len(dicts)):
				if i!=len(dicts)-1:
					wfile.write(str(dicts[i])+'\n,')
				else:
					wfile.write(str(dicts[i])+'\n')
			wfile.write(']')
			wfile.close()
			print(para)
			rfile=open('./json/'+str(para)+'-'+str(num)+'.json','r+',encoding='utf-8')
			rcontent=rfile.read()
			rcontent=rcontent.replace("'",'"')
			wfile=open('./json/'+str(para)+'-'+str(num)+'.json','w+',encoding='utf-8')
			wfile.write(rcontent)
		num+=1

	
# ~ 编号--code
# ~ 中文任务名字--name
# ~ 中文任务说明--desc
# ~ 奖励--bonus
# ~ 备注--memo
