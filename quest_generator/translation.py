#从excel生成任务
import pandas as pd
import json

#目前到出的list为字符串，需要用筛选剔除掉[]前后的引号引号。

"""
sheet_name用来指定选择哪个子表
header用来指定表头，默认0
默认为None，解析所有列。
如果为str，则表示Excel列字母和列范围的逗号分隔列表（例如“ A：E”或“ A，C，E：F”）。范围全闭。
如果为int，则表示解析到第几列。
如果为int列表，则表示解析那几列。
"""
getdata=pd.read_excel(r'quest_generator.xlsx',sheet_name="self.random_quest",header=0)

#显示前四行数据
#getdata.head()

#显示各项名字，行数 ，每列的数据数量
print(getdata.info())

print(getdata.values[1][0])

random_quests = []


for i in range(1,len(getdata)):
    dict={
    'id':1,
    "fields":{
        "description":"任务简介",
        "type":"检定类型wealth,strength,Ingenuity,Cyber",
        "value":"检定数值",
        "succeed":"检定成功文本",
        "fail":"检定失败文本",
        "succeed_type":[],
        "succeed_value":[],
        "fail_type":[],
        "fail_value":[],
        }
    }
    dict['id'] = getdata.values[i][0]
    dict['fields']['description'] = getdata.values[i][1]
    dict['fields']['type'] = getdata.values[i][2]
    dict['fields']['value'] = getdata.values[i][3]
    dict['fields']['succeed'] = getdata.values[i][4]
    dict['fields']['fail'] = getdata.values[i][5]
    dict['fields']['succeed_type'] = getdata.values[i][6]
    dict['fields']['succeed_value'] = getdata.values[i][7]
    dict['fields']['fail_type'] = getdata.values[i][8]
    dict['fields']['fail_value'] = getdata.values[i][9]
    random_quests.append(dict)
    
print(random_quests[2])

filename = 'quest_translation.txt'
with open(filename,'w',encoding='utf_8') as f:
    for i in range(len(random_quests)):
        f.write('{\n')
        for k,v in random_quests[i].items():
            f.write(f"\'{str(k)}\':{str(v)},\n")
        f.write('},\n')
    f.write(' \n')
        
f.close()
        