import random

class Character:

    def __init__(self, dmg, health, name):
        self.dmg = dmg
        self.health = health
        self.name = name

    def attack(self, enemy):
        enemy.takeDmg(self.dmg)
        if enemy.health <= 0:
            enemy.health = 0
            print(enemy.name + " is dead")


    def takeDmg(self, damage):
        self.health -= damage




class Monster(Character):

    def __init__(self, dmg, health, name):
        super().__init__(dmg, health, name)


class Hero(Character):

    MAX_HEALTH = 50
    xp = 0
    lvl = 1
    xpToLvls = [10, 20, 30, 40, 50]
    xp_to_next_lvl = xpToLvls[lvl-1]

    def __init__(self, dmg=10, health=30, name="Hero"):
        #dmg = 10
        #health = 30
        #name = "Hero"
        super().__init__(dmg, health, name)
        #self.MAX_HEALTH = 50

    def rest(self):
        if self.health >= self.MAX_HEALTH:
            print("No need of rest")
            return
        print("Resting...")
        print("Original health: ", self.health)
        #self.health = self.MAX_HEALTH
        self.health += 10
        if self.health >= self.MAX_HEALTH:
            self.health = 50
        print("Rested")
        print("Final health ", self.health)

    def lvlup(self):
        self.xp += 10
        if self.xp is self.xp_to_next_lvl:
            self.lvl += 1
            print("Level up!!! Level is ", self.lvl)
            self.xp_to_next_lvl = self.xpToLvls[self.lvl - 1]
            self.xp = 0

    def attack(self, enemy):
        super().attack(enemy)
        if enemy.health is 0:
            self.lvlup()

    def __str__(self):
        return 'Name: %s\nHealth: %d\nLevel: %d\nXP towards level %d: %d/%d' % (self.name, self.health, self.lvl, (self.lvl +1),  self.xp, self.xp_to_next_lvl)


class Goblin(Monster):

    def __init__(self, dmg=5, health=10, name="Goblin"):
        #dmg = 5
        #health = 10
        #name = "Goblin"
        super().__init__(dmg, health, name)

    def __str__(self):
        return 'Name: %s\nHealth: %d' % (self.name, self.health)


class Orc(Monster):

    def __init__(self, dmg=10, health=20, name="Orc"):
        #dmg = 10
        #health = 20
        #name = "Orc"
        super().__init__(dmg, health, name)

    def __str__(self):
        return 'Name: %s\nHealth: %d' % (self.name, self.health)


def explore():
    monsterType = random.choices([Goblin(), Orc(), None], [0.4, 0.1, 0.5], k=1)
    return monsterType[0]


if __name__ == "__main__":
    """hero = Hero(10, 30, "Hero")
    goblin = Goblin(5, 10, "Goblin")
    orc = Orc(10, 20, "Orc")
    hero.rest()
    hero.rest()
    hero.rest()
    print("Hero health in starting: ", hero.health)
    print("Goblin attacked")
    goblin.attack(hero)
    print("Hero health: ", hero.health)
    hero.rest()
    print("Orc attacked")
    orc.attack(hero)
    print("Hero health: ", hero.health)
    print("Hero attacked goblin.")
    hero.attack(goblin)
    print("Orc attacked Hero")
    orc.attack(hero)
    print("Hero health: ", hero.health)
    print("Orc health left: ", orc.health)
    print("Hero attacked Orc twice")
    hero.attack(orc)
    hero.attack(orc)
    print("Hero is victorious. Final health: ", hero.health)
    hero.rest()"""
    hero = Hero(10, 30, "Hero")
    goblin = Goblin(5, 10, "Goblin")
    orc = Orc(10, 20, "Orc")
    monster = explore()
    if monster is not None:
        print(monster.name+" appeared!")
        print("Hero attacked monster.")
        hero.attack(monster)
        print(monster)
        print(hero)
        for i in range(2):
            if monster.health != 0:
                print(monster.name + " attacked hero")
                monster.attack(hero)
                print(hero.name + " attacked the monster")
                hero.attack(monster)
    else:
        print("No monster found")










