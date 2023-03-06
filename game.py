import math
import random
class Warrior:
    def __init__(self,name="warrior",health=0,max_attack=0,max_block=0):
        self.name=name
        self.health=health
        self.max_attack=max_attack
        self.max_block=max_block
    def attack(self):
        attack_amt=self.max_attack*(random.random()+0.5)
        return attack_amt
    def block(self):
        block_amt=self.max_block*(random.random()+0.5)
        return block_amt
class Battle:
    def start_fight(self,warrior1,warrior2):
        while True:
            if self.get_attack_result(warrior1,warrior2)=="Game Over":
                print("-!Game Over!-")
                break
            if self.get_attack_result(warrior2,warrior1)=="Game Over":
                print("-!Game Over!-")
                break

    @staticmethod
    def get_attack_result(warrior1,warrior2):
        attack_a_amt=warrior1.attack()
        block_b_amt=warrior2.block()
        damage_b_amt=math.ceil(attack_a_amt-block_b_amt)
        warrior2.health=warrior2.health-damage_b_amt
        print("{} attack {} and deals {} damage".format(warrior1.name,warrior2.name,damage_b_amt))
        print("{} health down to {}".format(warrior2.name,warrior2.health))
        if warrior2.health<=0:
            print("{} is died and {} is winner".format(warrior2.name,warrior1.name))
            return "Game Over"
        else:
            return "Fight Again"
def main():
    raki=Warrior("Raki",50,20,10)
    rambo=Warrior("rambo",50,20,10)
    battle=Battle()
    battle.start_fight(raki,rambo)
main()

