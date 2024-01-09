#字串
a = 'hello'
b = 'world'
print(a+b)
print(a*3)
print(a[0], a[-1])

a = list(map(int,'10 20 30'.split() ))
print(a)

c = ['hello', 'world', 'very', 'good']
print(c[0]+c[1])
print( '###'.join(c) )