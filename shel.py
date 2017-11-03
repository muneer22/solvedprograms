import shelve
s=shelve.open("MyShelve")
s["company name"]="Applied Informatics"
s["company address"]= "Nigeen Srinagar"
for key in s:
	print(key)

s.close()
