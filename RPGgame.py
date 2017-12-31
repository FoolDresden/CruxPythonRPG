class Character:

    def __init__(self, dmg, health, name):
        self.dmg = dmg
        self.health = health
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.dmg
        if enemy.health <= 0:
            print(enemy.name + " is dead")

    def takeDmg(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(self.name + " is dead")


class Hero(Character):

    def __init__(self, dmg=10, health=30, name="Hero"):
        #dmg = 10
        #health = 30
        #name = "Hero"
        super().__init__(dmg, health, name)
        self.MAX_HEALTH = 50

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


class Goblin(Character):

    def __init__(self, dmg=5, health=10, name="Goblin"):
        #dmg = 5
        #health = 10
        #name = "Goblin"
        super().__init__(dmg, health, name)


class Orc(Character):

    def __init__(self, dmg=10, health=20, name="Orc"):
        #dmg = 10
        #health = 20
        #name = "Orc"
        super().__init__(dmg, health, name)


if __name__ == "__main__":
    hero = Hero(10, 30, "Hero")
    goblin = Goblin(5, 10, "Goblins")
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
    print("Hero attacked Orc thrice")
    hero.attack(orc)
    hero.attack(orc)
    print("Hero is victorious. Final health: ", hero.health)
    hero.rest()



