a,b,c = map(int, input())
d,e,f = map(int, input())

fisrt = (a*100 + b*10 + c) * f
second =(a*100 + b*10 + c) * e
third = (a*100 + b*10 + c) * d

print(fisrt)
print(second)
print(third)
print(fisrt+(second*10)+(third*100))
