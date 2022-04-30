import sys
import sys
import random
import time

from settings import Settings
from script import Script
from events import Events

day = 0

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
        print("Beta0.0.5\n")
        #开始界面
        self.prologue()
        while self.settings.game:
            #数值
            self.update()
            #检查输入框
            self._check_input()
            #当前主事件
            self.total_game()
            #检查是否解封
            self._check_end()
            self._check_states()
            self.debug()
            #自动游戏后加入时间间隔
            if self.autogame == 1:
                time.sleep(self.sleeptime)
        if self.settings.ending:
            self.ending()
        input("\n按任意键退出游戏。")
    
    def update(self):
        global day
        day+=1
        self.settings.day += 1
        self.settings.luck = random.randint(1,10)
        
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
                                    
    def total_game(self):
        
        """决定选择哪个主事件"""
        if self.settings.beggining:
            #主线
            self.main_game()
        elif self.settings.arc_game:
            #方舱事件
            self.arc_game()
        
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
        self.settings.eggs -=2
        if self.settings.eggs <=0:
            self.settings.mood -= 1
            self.settings.eggs = 0

        if self.settings.immune <=0 and self.settings.day+7 <self.settings.days :
            print(self.script.positive)
            self.settings.beggining = False
            self.settings.arc_game = True

    
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
            if self.settings.luck >5:
                print(self.script.negative1)
            else:
                print(self.script.negative2)
            
    def _check_begin(self):
        """游戏开始前数值初始化"""
        str = input("是否开始游戏？(y/n)")
        if str =='y':
            self.settings.prologue = False
            self.settings.beggining = True
            self.settings.game = True
            self.settings.immune = self.settings.strength
            self.settings.eggs = self.settings.wealth*3+10
            print("\n当我年轻的时候，我记得任何事情，无论它是否发生过。——马克.吐温")
            
        elif str == 'n':
            self.prologue()
        else:
            print("请输入正确的选择(y/n)")
            self._check_begin()
            
    def _check_end(self):
        """检查封锁日期"""
        if self.settings.day == self.settings.days:
            self.clear_all()
            self.settings.ending =True
            
    def ending(self):
        """尾声和分支结局"""
        
        print(self.script.end_1)
        
        #print(self.settings.reputation)
        if self.settings.reputation >= 3:
            print(self.script.end_reputation)
                
        if self.settings.friendship_zmz:
            print(self.script.end_zmz)
            
        if self.settings.mood>60:
            print(self.script.end_mood)
        else:
            print(self.script.end)
        
    def _check_input(self):
        """输入检查"""
        while self.autogame == 0:
            self.input = input("\n...任意键继续，按a自动游戏，按e退出游戏...")
            if self.input == 'a':
                self.autogame =1
            elif self.input =='e':
                self.clear_all()
                print("\n游戏终止，感谢您进行游戏。")                    

            break
            
    def clear_all(self):
        """清理所有主循环的flag,给结尾制造条件"""
        self.settings.beggining = False
        self.settings.arc_game = False
        self.settings.game = False
    
    def _get_information(self):
        """自定义人物部分"""
        print("四项属性上限为20点。")
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

            print(f"您的壕力为{self.settings.wealth}")
            print(f"您的体格为{self.settings.strength}")
            print(f"您的才智为{self.settings.Ingenuity}")
            print(f"您的网龄为{self.settings.Cyber}\n")

            self._check_begin()
            
    def debug(self):
        #print(f"\n免疫值：{self.settings.immune},鸡蛋数目：{self.settings.eggs},心情：{self.settings.mood}\n运气：{self.settings.luck},声望：{self.settings.reputation}")
        print(f"\n健康：{self.settings.immune},心情：{self.settings.mood},声望：{self.settings.reputation}")

if __name__ == '__main__':
    siege = Game()
    siege.run_game()