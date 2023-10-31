#剝皮法
a = 1234
ans = 0 #答案，把剝下來的皮放進去
while a>0:
  ans = ans*10 + a%10
  print('現在的a是' ,a ,'剝出來的皮a%10是' ,a%10 ,'現在的ans就變成' ,ans)
  a = a // 10