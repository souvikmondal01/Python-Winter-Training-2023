class SuperHero():
    def __init__(self, name, superPower):
        self.name = name
        self.superPower = superPower

    def getSuperPower(self):
        print(f"I am {self.name} and my power is {self.superPower}")


ironMan = SuperHero(name="Ironman", superPower="Suit")
ironMan.getSuperPower()

thor = SuperHero(name="Thor", superPower="Hammer")
print(thor.name)
print(thor.superPower)
thor.getSuperPower()
