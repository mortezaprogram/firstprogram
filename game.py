import math
import random
class Warrior:
    def __nit__(self,name="warrior",health=0,max_attack=0,max_block=0):
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