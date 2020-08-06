print('checking profit or loos of product')


#initialisng a class product
class product:
	product_tracking = "http://www.google.com"

	#initialisng a method
	def __init__(self, name, texture, sp):
		self.name = name
		self.texture = texture 
		self.sp = sp
		self.cost_price = 500

	
	#method - profit
	def profit (self, things):
		things.profit = things.sp - self.cost_price
		print(things.name,'profits are $',things.profit)

	#method - loss
	def loss (self, things):
		things.loss = self.cost_price - things.sp
		print(things.name, 'losses are $',things.loss)
    

#objects instantiation 
metal = product('gold','hard', 600)
snacks= product('fruits','soft',300)


#calling objects 
#object.method
print(metal.name)
print(snacks.name)
print(snacks.texture)
print(metal.texture)
print(metal.sp)
print(metal.cost_price)
print(snacks.sp)
print(snacks.cost_price)

#calling object - class.method
print(product.product_tracking)

#if else loop with conditions
if (metal.sp | snacks.sp > 500 ) :
	snacks.profit(metal)
	
else :
	metal.loss(snacks)

