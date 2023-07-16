class game:
	
	def __init__(ouch, a,b):
		ouch.level1 = a
		ouch.level2 = b
		
	def __add__(gamer1, gamer2):
		obj = game(gamer1.level1 + gamer2.level1,gamer1.level2 + gamer2.level2)
		return obj

	def __str__(a):
		return "LEVEL 1 SCORE: " + str(a.level1) + "\nLEVEL 2 SCORE: " + str(a.level2)
		


gmr1 = game(100,200)
gmr2 = game(400,100)

#combine

ttl = gmr1+gmr2

print(ttl)