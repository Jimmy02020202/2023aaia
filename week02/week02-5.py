a= input()
b = int(a)

if b>=90:
	ans = 'A'
if 80 <= b < 90:
	ans = 'B'
if 70 <= b < 80:
	ans = 'C'
if 60 <= b < 70:
	ans = 'D'
if 60 < b:
	ans = 'F'
	
print(ans, end='')