print("object oriented programming python")

# using __init__
class student: #student is a class name
	#initialising a method
	def __init__(self, name, num, age):  #method has 3 attributes
		self.name = name
		self.num = num
		self.age = age


class faculty:             #faculty is a class name
	#initialising a method
	def __init__(self, name, num, age): #method with 3 attributes
		self.name = name
		self.num = num
		self.age = age
# harika, nitara, cheguvera, hasini are the objects
harika = student('harika', 1000, 25)
nitara = faculty('nitara', 'fac1', 30)
cheguvera = faculty('cheguvera', 'head1', 40)
hasini = student('hasini', 'a2', 23)

#calling harika details from student class
print(harika.name)
print(harika.num)
print(harika.age)

#calling nitara details from faculty class
print(nitara.name)
print(nitara.num)
print(nitara.age)

#calling hasini details from student class
print(hasini.name)
print(hasini.num)
print(hasini.age)

#calling cheguvera details from faculty class
print(cheguvera.name)
print(cheguvera.num)
print(cheguvera.age)
