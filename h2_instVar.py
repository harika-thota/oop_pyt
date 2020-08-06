print("class vs instant_variables") 

#starting a class 
class DogBreads:
	website = "https://petco.com"


#initialising a method 
	def __init__(self, name, colour):
		self.name = name 
		self.colour = colour 


#initialising objects
german_shepperd = DogBreads('german_shepperd', 'white')
husky = DogBreads('husky','black')

#calling object_name.method 
print(german_shepperd.name) 
print(husky.colour)

#calling class_name.method
print(DogBreads.website)
print(husky.name) #calling object_name.method

