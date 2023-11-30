#計算一組任意數目的整數的總和

N = int(input() )
a = list(map(int,input().split() ))
b = list(map(int,input().split() ))

for i in range(N):
    print( a[i] + b[i], end =' ')