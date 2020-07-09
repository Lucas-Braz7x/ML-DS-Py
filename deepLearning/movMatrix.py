#importando bibliotecas
import random

#DEFININDO CLASSES
class Point(object):

    def __init__(self, x, y):#Construtor da classe
        self.x = x
        self.y = y
    
    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)
class Reward(Point):
    
    def __init__(self, x, y, name):#Construtor da classe
        super(Reward, self).__init__(x,y)
        self.name = name
    
    def __str__(self):
        return '<%s, %s>: %s' % (self.x, self.y, self.name)

    def __repr__(self):
        return '<Reward> %s' % str(self)

class Robo(Point):#Definindo uma classe

    def __init__(self, x, y):#Construtor da classe
        super(Robo, self).__init__(x,y)

    def move_up(self):
        if self.y<10:
            self.y += 1
        else:
            print("Movimento proibido")

    def move_down(self):
        if self.y>0:
            self.y -= 1
        else:
            print("Movimento proibido")

    def move_left(self):
        if self.x>0:
            self.x -= 1
        else:
            print("Movimento proibido")
            
    def move_right(self):
        if self.x<10:
            self.x += 1 
        else:
            print("Movimento proibido")

#DEFININDO FUNÇÕES
def check_reward(robo, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robo.x and reward.y == robo.y:
            print("Recompensa achada = %s " % reward.name)
            ok = True
    return ok

reward1 = Reward(random.randint(0,10), random.randint(0,10),"Moeda de ouro")
reward2 = Reward(random.randint(0,10),random.randint(0,10),"Gasolina")
reward3 = Reward(random.randint(0,10),random.randint(0,10),"Espada flamejante")
reward4 = Reward(random.randint(0,10), random.randint(0,10),"Pilha")
reward5 = Reward(random.randint(0,10),random.randint(0,10),"Machado")
reward6 = Reward(random.randint(0,10),random.randint(0,10),"Armadura")
reward7 = Reward(random.randint(0,10), random.randint(0,10),"Carne")
reward8 = Reward(random.randint(0,10),random.randint(0,10),"Familiar")
reward9 = Reward(random.randint(0,10),random.randint(0,10),"Horse")

rewards = [reward1, reward2, reward3,reward4, reward5, reward6,reward7, reward8, reward9]
print("Recompensas criadas\n")

robo1 = Robo(random.randint(0,10),random.randint(0,10) )
print("Robo criado\n")

print("Interação com o usuário:\n")
for i in range(10):
    move = input("Digite up, down, left ou right para o movimento\n")
    if move == "up":
        robo1.move_up()
    elif move == "down":
        robo1.move_down()
    elif move == "left":
        robo1.move_left()
    elif move == "right":
        robo1.move_right()
    else:
        print("Movimento inválido\n")
        continue
    print(robo1)
    check_reward(robo1, rewards)




