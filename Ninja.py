from Pet import Cat,Dog,Bird,Pet

class Ninja :
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        
        
        self.treats=treats
        self.pet_food=pet_food
    
    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

Leo=Cat('Leo','Turkish','sleeping',100,100)
merya=Ninja('merya','bouaziz',Leo,'Croquettes','Dry food')

merya.walk()
print(Leo.health)
merya.bathe()

tweetie=Bird('Tweetie','Turkish','sleeping',100,100)
merya=Ninja('merya','bouaziz',tweetie,'Croquettes','Dry food')
merya.bathe()

Fox=Dog('Fox','Turkish','sleeping',100,100)
merya=Ninja('merya','bouaziz',Fox,'Croquettes','Dry food')
merya.bathe()