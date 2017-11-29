d={}
for i in range(int(input())):
	line=input().split()
	d[line[0]]=sum(map(float,line[1:]))/3
print ('%.2f' % d[input()])