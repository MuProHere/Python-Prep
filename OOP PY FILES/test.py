class bird:

	legs = 2

	def __init__(self):
		print("in bird")
		self.color = 'blue'
		self.reporg = self.reporg()

	@classmethod
	def lol(cls):
		return cls.legs

	def sum(self, a=None, b=None):
		return a + b

	class reporg:
		def __init__(self):
			self.org = 'peen'
			self.fld = 'trans'


cock = bird()

print(cock.sum(1))




"""class wh1:
		def __init__(self):
			print("in WH1")

class wh2(bird, wh1):
		def __init__(self):
			super().__init__()
			print("in WH2")			

cock = wh2()
"""
#print(cock.reporg.org)


#print(bird.lol())

"""cock = bird()
pcock = bird()

cock.legs = 10

print("cock: ", cock.legs)
print("peacock: ", pcock.legs)

bird.legs = 5

print("cock: ", cock.legs)
print("peacock: ", pcock.legs)"""
