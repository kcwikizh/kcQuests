import json
import os
rs={}
num=0
para=0

for para in range(3):
	num=0
	print(para)
	while(num!=100):
		if(os.path.isfile('./fineJson/'+str(para)+'-'+str(num)+'.json')):
			temp=open('./fineJson/'+str(para)+'-'+str(num)+'.json','r+',encoding='utf-8')
			content=temp.read()
			content=json.loads(content)
			for i in content:
				rs[i]=content[i]
		num+=1

rs=str(rs).replace("'",'"')
rs=json.loads(rs)
rs=json.dumps(rs,sort_keys=True,ensure_ascii=False,indent=2)	


output=open('./quests-scn.json','w+',encoding='utf-8')
output.write(str(rs))

output=open('./dist/quests-scn.json','w+',encoding='utf-8')
output.write(str(rs))


# 单独生成最新


new=2
num=0
newrs={}
while(num!=100):
	if(os.path.isfile('../fineJson/'+str(new)+'-'+str(num)+'.json')):
		print("new"+str(num))
		temp=open('../fineJson/'+str(new)+'-'+str(num)+'.json','r+',encoding='utf-8')
		content=temp.read()
		content=json.loads(content)
		for i in content:
			newrs[i]=content[i]
	num+=1

newrs=str(newrs).replace("'",'"')
newrs=json.loads(newrs)
newrs=json.dumps(newrs,sort_keys=True,ensure_ascii=False,indent=2)	


output=open('./quests-scn-new.json','w+',encoding='utf-8')
output.write(str(newrs))
output=open('./dist/quests-scn-new.json','w+',encoding='utf-8')
output.write(str(newrs))
