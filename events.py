import sys
import random
import time

from settings import Settings
from script import Script

class Events:
    
    def __init__(self,SoS):
        super().__init__()
        self.script = Script() 
        self.settings = SoS.settings
        
    def test(self):
        global day
        print(day)

    def cyber_events(self):
        '''赛博事件'''
        if self.settings.day == 1:
            print(self.script.cyber_firstday)
        else:
            event = random.randint(1,len(self.script.cyber_events2)-1)
            #print (f"回到寝室后，{self.script.cyber_events[event]}")
            print (f"回到寝室后，{self.script.cyber_events2[event]['description']}")
            exec(f"self.settings.{self.script.cyber_events2[event]['type']} += int(self.script.cyber_events2[event]['value']) ")    
            del self.script.cyber_events2[event]
            print("")

    def NA_events(self):
        
        if self.settings.day == 2:
            print("今天不需要做核酸。\n居委将试剂盒分装好，送到了楼下大堂。\n你被告知一天要测一次抗原,\n最后要将抗原结果传到小程序上。")
        
        elif self.settings.day == 10:
            print("你们被告知从今天开始每天要做两次抗原检测。")
            
        elif self.settings.day == 17:
            print("你被告知需要分别在8时、12时、16时与20时各做一次抗原检测。")
            
        elif self.settings.day == 20:
            print("一部分居民认为大规模核酸感染风险太高，拒绝前往。\n他们将抗原结果贴在门口，以证明自己是阴性。")
        
        else:
            
            if str(self.settings.day) not in self.script.days.keys():  
                clocks = '6点钟 7点钟 8点钟 9点钟 10点钟'.split()
                clock = random.randint(0,len(clocks)-1)
                print(f"你今天早上{clocks[clock]}被叫下来测核酸。" )
                if self.settings.luck<=5:
                    if self.settings.luck <3 :
                        print("你感觉再这么测下去，鼻粘膜都要被捅破了。")
                    else:pass

                else:
                    print("很幸运，今天只要捅喉咙。")
        print("")
        
    def important_events(self):
        """封城大事件"""
        if str(self.settings.day) in self.script.days.keys():
            print(self.script.days[str(self.settings.day)])
            
    def operations_events(self):
        """全面攻坚"""
        if str(self.settings.day) in self.script.operations.keys():
            print(f"上面要求{self.script.operations[str(self.settings.day)]}\n")  
       
    def random_events(self):
        """日常随机事件"""
        
        if str(self.settings.day) not in self.script.days.keys():
            quest = random.randint(1,len(self.script.random_quests[self.settings.mode])-1)
            #检查数值传递
            print(self.script.random_quests[self.settings.mode][quest]['fields']['description'])
            if eval('self.settings.'+self.script.random_quests[self.settings.mode][quest]['fields']['type']) >= int(self.script.random_quests[self.settings.mode][quest]['fields']['value']):
                #debug用，查看list长度
                #print(len(self.script.random_quests[quest]['fields']['succeed_type']))
                print (f"\n【判定成功】：\n{self.script.random_quests[self.settings.mode][quest]['fields']['succeed']}")                
                for i in range(0,len(self.script.random_quests[self.settings.mode][quest]['fields']['succeed_type'])):
                    exec(f"self.settings.{self.script.random_quests[self.settings.mode][quest]['fields']['succeed_type'][i]} += int(self.script.random_quests[self.settings.mode][quest]['fields']['succeed_value'][i]) ")                
            else:
                #print(len(self.script.random_quests[quest]['fields']['fail_type']))
                print (f"\n【判定失败】：\n{self.script.random_quests[self.settings.mode][quest]['fields']['fail']}")                
                for i in range(0,len(self.script.random_quests[self.settings.mode][quest]['fields']['fail_type'])):
                    exec(f"self.settings.{self.script.random_quests[self.settings.mode][quest]['fields']['fail_type'][i]} += int(self.script.random_quests[self.settings.mode][quest]['fields']['fail_value'][i]) ")
                #print("\n")
            del self.script.random_quests[self.settings.mode][quest]
            #等事件够了再用。
            print("")
           
    def arc_events(self):
        """方舱随机事件"""        
        quest = random.randint(1,len(self.script.arc_quests)-1)
        #检查数值传递        
        #print(self.script.arc_quests[quest]['id'])
        print(self.script.arc_quests[quest]['fields']['description'])
        if eval('self.settings.'+self.script.arc_quests[quest]['fields']['type']) >= int(self.script.arc_quests[quest]['fields']['value']):
            #debug专用，查看list长度
            #print(len(self.script.arc_quests[quest]['fields']['succeed_type']))
            print (f"\n【判定成功】：\n{self.script.arc_quests[quest]['fields']['succeed']}")                
            for i in range(0,len(self.script.arc_quests[quest]['fields']['succeed_type'])):
                exec(f"self.settings.{self.script.arc_quests[quest]['fields']['succeed_type'][i]} += int(self.script.arc_quests[quest]['fields']['succeed_value'][i]) ")                
        else:
            #print(len(self.script.arc_quests[quest]['fields']['fail_type']))
            print (f"\n【判定失败】：\n{self.script.arc_quests[quest]['fields']['fail']}")                
            for i in range(0,len(self.script.arc_quests[quest]['fields']['fail_type'])):
                exec(f"self.settings.{self.script.arc_quests[quest]['fields']['fail_type'][i]} += int(self.script.arc_quests[quest]['fields']['fail_value'][i]) ")
            #print("\n")
        del self.script.arc_quests[quest]   
     
    def sleep_events(self):
        
        if self.settings.mood >= 60:
            print("不管怎么说，你今晚的心情还算可以,\n你决定多打一会游戏再睡觉。")
            """
            game = random.choice(self.settings.games)
            print(f"你所游玩的游戏名叫{game}")
            """
        
        elif self.settings.mood >= 45:
            dream = random.choice(self.script.dreams)
            print(dream)
            
        else :
            nightmare = random.choice(self.script.nightmares)
            print(nightmare)
            
            
