print('Topic - String representation')

#initialising a class 
class students:
	institute = "AYUH INTERNATIONAL ACADEMY"

	#initialising a method 
	def __init__ (self, name, num, gender):
		self.name = name 
		self.num = num 
		self.gender = gender
    #initialising a string method 
	def __str__ (self):
		return "{} : {} : {} ".format(self.name,self.num,self.gender)

#instantiating object 
wook = students('ji chang wook' , 1 ,' male')
harika = students('harika thota' , 2, 'female')

#calling object 
print(wook, harika) 
