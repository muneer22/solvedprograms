a=[["Harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]] 
#for a in range(int(input())):
#	name=input()
#	score=float(input())

s=sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1] == s[1]):
	print(name)
