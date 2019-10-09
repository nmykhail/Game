import random
class Unit:
    def __init__(self, health, power, name, armor):
        self.health = health
        self.power = power
        self.name = name
        self.armor = armor
#Здоров'я Unit
    def get_health(self):
        return self._health

    def set_healt(self, value):
        if value < 0 or type(value) != int:
            print("Error value health")
            self._health = 1
        else:
            self._health = value

    health = property(get_health, set_healt)
#Сила Unit
    def get_power(self):
        return self._power

    def set_power(self, value):
        if value < 0 or type(value) != int:
            print("Error value power")
            self._power = 1
        else:
            self._power = value

    power = property(get_power, set_power)
#Броня Unit
    def get_armor(self):
        return self._armor

    def set_armor(self, value):
        if value < 0 or type(value) != int:
            print("Error value armor")
            self._armor = 1
        else:
            self._armor = value

    armor = property(get_armor, set_armor)
#Атака: спочатку віднімається броня, потім - здоров'я
    def attack(self, enemy):
        if (enemy.health + enemy.armor) > self.power:
            if enemy.armor > self._power:
                enemy.armor -= self.power
            elif enemy.armor <= self.power:
                enemy.health -= (self.power - enemy.armor)
                enemy.armor = 0
        else:
            enemy.health = 0

u1 = Unit(power=9, health=50, armor=15, name="Tamplier")
u2 = Unit(power=9, health=50, armor=15, name="Assassin")
print("Name :", u1.name, "Health :", u1.health, "Power :", u1.power, "Armor :", u1.armor)
print("Name :", u2.name, "Health :", u2.health, "Power :", u2.power, "Armor :", u2.armor)

class Battle:
    @staticmethod
    def fight(attacker, defender):
        while attacker.health != 0 and defender.health != 0:
            if attacker.health > 0:
                attacker.attack(defender)
            else:
                print(defender.name, " is dead!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
            if defender.health > 0:
                defender.attack(attacker)
            else:
                print(attacker.name, " is dead!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
            print("Attack :", attacker.name, "with power :", attacker.power)
            print(attacker.name +' health is '+str(attacker.health)+' power is '+str(attacker.power)+' armor is '+str(attacker.armor))
            print("Attack :", defender.name, "with power :", defender.power)
            print(defender.name +' health is '+ str(defender.health)+' power is '+str(defender.power)+' armor is '+str(defender.armor))

players = random.sample([u1, u2], 2)
Battle.fight(players[0], players[1])