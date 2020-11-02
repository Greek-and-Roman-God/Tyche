n,k = map(int, input().split())
cnt = 0

while 1 :
    if n == 1 : #사용자가 입력한 n이 1일때 먼저 거르고 반복을 거쳐 n = 1되면 break로 빠져나오기
        break
    elif n % k == 0 :
        n /= k 
        cnt +=1
    elif n % k != 0 :
        n -= 1
        cnt +=1

   
print(cnt)