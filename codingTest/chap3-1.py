n = 1260
cnt = 0

coin = [500,100,50,10]

for coin in coin :
  cnt += n //coin # n(거스름돈)을 coin으로 나눈 몫을 누적!!! 
  n %= coin

print(cnt)