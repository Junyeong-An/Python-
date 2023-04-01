
class human:
    def status(self,MP,HP):
        self.MP = MP
        self.HP = HP


    def meet(self):
        print("human: 안녕하세요")


class player(human):
    
    def __init__(self,AD):
        self.AD=AD

    def att(self,enemy):
        damage=self.AD-enemy1.DP
        enemy1.HP=enemy1.HP-damage


class enemy(human):
    def __init__(self,DP):
        self.DP = DP


class npc(human):
    def meet(self):
        print("NPC를 만났다\nNPC: 반갑습니다")



npc1=npc()
player1= player(100)
enemy1= enemy(50)

player1.status(100,100)
enemy1.status(100,100)

while True:
    a=input("1이나 2를 입력\n")

    if a == "1":
        player1.meet()
        npc1.meet()
        continue
    elif a == "2":
        player1.att(enemy)
        print("enemy를 공격했다")
        if enemy1.HP == 0:
            print("enemy의 HP가 0이 되서 종료")
            break
        continue





    break

