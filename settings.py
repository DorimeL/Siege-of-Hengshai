class Settings:  
    
    def __init__(self):
        '''游戏中的初始化设置'''
        self.days = 32
        self.positive_days =7

        #四大数值设置
        self.wealth = 5
        self.strength = 5
        self.Ingenuity = 5
        self.Cyber = 5
        
        #其它杂七杂八的数值
        self.default = 100
        self.money = 10000
        self.health = 100
        self.immune = 5
        self.eggs = 0
        self.cola = 5
        self.mood = 60
        self.luck = 10
        self.reputation = 0
                
        self.day = 0
        self.arc_day = 0
        #自动间隔时间
        self.sleeptime = 2 
        
        #检定flag
        self.end_arc = False
        self.end_travel = False
        
        self._check_eggs = True
        self._check_mood = True
        
        #事件flag
        self.mode = 0
        self.prologue = True
        self.game = False
        self.beggining = False
        self.arc_game = False
        self.ending = False
       
        
        #好感度
        self.friendship_zmz = 0
        
        #游戏库
        self.games = 'The_Witness The_Fish_Fillets_2 A_Monster\'s_Expedition Stephen\'s_Sausage_Roll Baba_Is_You 5_Steps_Steve The_Golem Room_to_Grow Jack_Lance_games Serpent_Fusion Understand Yet_Another_Pushing_Puzzler YAPP:_Yet_Another_Puzzle_Platformer Kine SOLAS_128 Snaliens Puddle_Knights Markov_Alg Induction A_Good_Snowman_Is_Hard_To_Build Sensorium Pipe_Push_Paradise Hiding_Spot Recursed DROD Campfire_Cooking Jelly_no_Puzzle Hanano_Puzzle Fish_Fillets_-_Next_Generation English_Country_Tune Snakebird Worm_Jazz Altered Tametsi Hexcells YANKAI\'S_PEAK Syzygy Sokobond Push_Blox_2 B.i.t.Lock Tricone_Lab Spring_Fall Filament Couch_Installation_Service Little_Square_Things Princess_Castle_Quest'.split()
        


        #废案
        self.special_day = [1,2,3,5,6,10,20,25]
        
