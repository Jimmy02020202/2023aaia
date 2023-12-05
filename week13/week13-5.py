a = list(map(int,input().split() ))

print( min(a) )


a = list(map(int,input().split() ))

for i in range(6):
	print(a[i]*a[i]*a[i])
    
    
a = int(input())

for i in range(2,a+1,2):
	print(i,end= ' ')
	
    
a = list(map(int,input().split() ))

print(f'[{min(a)},{max(a)}]' , end='')