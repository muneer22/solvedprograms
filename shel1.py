import shelve
s= shelve.open("MyShelve")
print(s["company name"])
print(s["company address"])
