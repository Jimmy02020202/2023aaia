a = list(map(int,input().split() ))
fast = min(a)

for i in range(len(a)):
	if a[i]==fast:
		ans = i + 1
		break
	
print(ans, int(1.2*60*60/fast) )