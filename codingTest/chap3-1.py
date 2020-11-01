n = 1260
cnt = 0

money = [500,100,50,10]

for money in money :
  cnt += n //money # n(거스름돈)을 money으로 나눈 몫을 누적!!! 
  n %= money #n을 coin으로 나눈 나머지를 n으로 다시 저장 

print(cnt)