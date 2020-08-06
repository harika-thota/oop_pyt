print('Topic - Methods in class')

#initialising fighters class
class fighters:

	#initialising init method with a argument 
	def __init__(self, name):
		self.name = name 
		self.health = 100
		self.damage = 10 

	#initalising another method-attackers
	def attackers(self, opponent):
		opponent.health = opponent.health - self.damage  

#object instantiation
human = fighters('Harika')
animal = fighters('Lion')

#object calling
print(human.name,'is human and her health is',human.health )
print(animal.name,'is animal and her health is', animal.health)

animal.attackers(human)

print('after attack', human.health,'is harikas health')


