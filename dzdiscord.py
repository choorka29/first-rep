import random
 
class Soldiers():
    id = 1
    def unit(self):      
        self.id_ = Soldiers.id
        Soldiers.id += 1
 
    def go_hero(self,hero):
        print(f'солдат с id {self.id} следует за героем {hero.id}')
        
    def str(self):
        return f'{self.id}'
    
class Heroes(Soldiers):
    
    def unit(self, team):
        Soldiers.unit(self)
        self.team = team
        self.level = 0
 
    def level_up(self):
        self.level += 1
        print(f'герой с id {self.id_} достиг {self.level} уровня')
    
red_heroes = Heroes('red')
blue_heroes = Heroes('blue')
list_red_heroes = []
list_blue_heroes = []
for _ in range(50):
    if random.choice(['red', 'blue']) == 'red':
        list_heroes.append(Soldiers())
    else:
        list_blue_heroes.append(Soldiers())
        
len_red_heroes = len( list_red_heroes)
len_blue_heroes = len( list_blue_heroes) 
print(f'солдат у героя red_heroes - {len_red_heroes}')
print(f'солдат у героя blue_heroes - {len_blue_heroes}')
if len_red_heroes > len_blue_heroes:
    red_heroes.level_up()
else:
    blue_heroes.level_up()
 
random.choice(list_red_heroes).go_hero(red_heroes)
