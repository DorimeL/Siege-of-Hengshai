import sys
import random
import time

from settings import Settings
from script import Script
from events import Events

class Game:
    
    def __init__(self):
        
        self.settings = Settings()
        self.script = Script()
        self.events = Events(self)

        self.autogame = 0
        self.input = 0
        #自动间隔时间
        self.sleeptime = 2 
           
    def run_game(self):
        """游戏主循环"""
        print("|||———————————————————-|||")
        print(self.script.title)
        print("|||__________SIEGE--OF--HENGSHAI__________|||")
        #开始界面
        self.prologue()
        while self.settings.game:
            #数值
            self.update()
            #当前主事件
            self.total_game()
            #检查是否解封
            self._check_end()
            self._check_states()
            self.debug()
            #自动游戏后加入时间间隔
            #检查输入框
            self._check_input()
            if self.autogame == 1:
                time.sleep(self.sleeptime)
        if self.settings.ending:
            self.ending()
        input("\n按任意键退出游戏。")
    
    def update(self):

        self.settings.day += 1
        self.settings.luck = random.randint(1,10)
        
        #鸡蛋
        if self.settings.beggining:
            self.settings.eggs -=2
            if self.settings.eggs <=0:
                self.settings.mood -= 1
                self.settings.eggs = 0
        #根据日期切换城市状态。
        if self.settings.day == 5:
            self.settings.mode = 1
            
        elif self.settings.day ==20:
            self.settings.mode = 2
                                    
    def total_game(self):
        
        """决定选择哪个主事件"""
        if self.settings.arc_game:
            #方舱
            self.arc_game()
        else:
            #主事件
            self.main_game()
        
    def main_game(self):
        
        """主要故事线"""
        print(f"\n【今天是封城的第{self.settings.day}天】")
        self.events.operations_events()
        self.events.important_events()
        self.events.NA_events()
        self.events.random_events()
        self.events.cyber_events()
        self.events.sleep_events()
        #self._check_hungry()
        #阳性检定
        self._check_positive()
    
    def arc_game(self):
        
        """方舱故事线"""
        self.settings.arc_day +=1
        print(f"\n【今天是封城的第{self.settings.day}天】")
        print(f"【今天是来到方舱后的第{self.settings.arc_day}天】")        
        self.events.arc_events()
        #出舱判定
        if self.settings.arc_day ==self.settings.positive_days :
            self.settings.beggining = True
            self.settings.arc_game = False
            self.settings.immune = 10
            print(self.script.negative1)
                
            
    def _check_begin(self):
        """游戏开始前数值初始化"""
        str = input("是否开始游戏？(y/n)")
        if str.upper() =='Y':
            self.settings.prologue = False
            self.settings.beggining = True
            self.settings.game = True
            self.settings.immune = self.settings.strength
            self.settings.eggs = self.settings.wealth*3+10
            sys.stdout = Logger("my_diary.txt")
            print("\n当我年轻的时候，我记得任何事情，无论它是否发生过。——马克.吐温")
            
        elif str.upper() == 'N':
            self.prologue()
        else:
            print("请输入正确的选择(y/n)")
            self._check_begin()
            
    def _check_end(self):
        """检查封锁日期"""
        if self.settings.day == self.settings.days:
            self.clear_all()
            self.settings.ending =True
            
    def _check_states(self):
        
        while self.settings._check_eggs and self.settings.beggining:
            
            if self.settings.eggs <=0:
                print("\n你消耗完了所有的鸡蛋，失去了重要的蛋白质补充。\n你的免疫力下降了，你的心情也开始变得更糟。")
                self.settings.immune -=1
                self.settings._check_eggs = False
            break
            
        while self.settings._check_mood:
            if self.settings.mood <=0:
                print("\n高压下的生活让你的心情跌倒了极点。\n你的免疫力下降了。")
                self.settings.immune -=1
                self.settings._check_mood = False
            break
        if self.settings.mood <=0:
            self.settings.mood = 0
            
    def _check_input(self):
        """输入检查"""
        while self.autogame == 0:
            self.input = input("\n...任意键继续，按a自动游戏，按e退出游戏...")
            if self.input.upper() == 'A':
                self.autogame =1
            elif self.input.upper() =='E':
                self.clear_all()
                print("\n游戏终止，感谢您进行游戏。")                    

            break

    def _check_positive(self):
        """阳性检测"""
        if self.settings.immune <=0 and self.settings.day+7 <self.settings.days :
            print(self.script.positive)
            self.settings.end_arc = True
            if self.settings.luck >8:
                #会展中心。
                print(self.script.positive_luck)
            else:
                #无家可归。
                print(self.script.positive_fuck)
                input("")
                print(self.script.positive_fuck2)
                input("")
                print(self.script.positive_fuck3)
                self.settings.mood -=20
                self.settings.end_travel =True
                
            self.settings.beggining = False
            self.settings.arc_game = True
            
    def clear_all(self):
        """清理所有主循环的flag,给结尾制造条件"""
        self.settings.beggining = False
        self.settings.arc_game = False
        self.settings.game = False
    
    def _get_information(self):
        """自定义人物部分"""
        print("\n欢迎游玩本游戏，请定制你的人物，\n你的人物属性会影响游戏进程。\n【四项属性上限为20点】")
        try:
            self.settings.wealth = abs(int(input("请选择你的壕力")))
            self.settings.strength = abs(int(input("请选择你的体格")))
            self.settings.Ingenuity = abs(int(input("请选择你的才智")))
            self.settings.Cyber = 20 - self.settings.wealth -self.settings.strength - self.settings.Ingenuity 
        except ValueError:
            print("\n识别失败，请输入数字")
            self._get_information()
                
    def prologue(self):
        '''开始界面'''
        while self.settings.prologue:
            self._get_information()

            if self.settings.Cyber < 0 :
                print("\n超出最大分配点数！")
                continue

            print(f"\n您的壕力为{self.settings.wealth}")
            print(f"您的体格为{self.settings.strength}")
            print(f"您的才智为{self.settings.Ingenuity}")
            print(f"您的网龄为{self.settings.Cyber}\n")

            self._check_begin()
            
    def ending(self):
        """尾声和分支结局"""       
        print(self.script.end_1)
        input('')
        #print(self.settings.reputation)
        if self.settings.reputation >= 3:
            print(self.script.end_reputation)
            input('')
        
        #方舱分支
        if self.settings.end_arc == True:
            print(self.script.end_arc)
            input('')
            if self.settings.end_travel ==True:
                print(self.script.end_arc_travel)
                input('')
        else:
            print(self.script.end_arc_none)
            input('')
            
        #张麻子
        if self.settings.friendship_zmz:
            print(self.script.end_zmz)
            input('')
        
        if self.settings.mood>60:
            print(self.script.end_mood)
        else:
            print(self.script.end)
            
    def debug(self):
        #print(f"\n免疫值：{self.settings.immune},鸡蛋数目：{self.settings.eggs},心情：{self.settings.mood}\n运气：{self.settings.luck},声望：{self.settings.reputation}")
        print(f"\n健康：{self.settings.immune},心情：{self.settings.mood},声望：{self.settings.reputation}，城市紧张度：{self.settings.mode+1}，垃圾桶：{self.settings.default}")


#储存任务日记
class Logger(object):

    def __init__ (self, fileN="Default.1og"):
        self.terminal = sys.stdout
        self.log = open(fileN,"w",encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass        

#
if __name__ == '__main__':
       
    siege = Game()
    siege.run_game()