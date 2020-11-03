#볼링공 고르기
#서로다른 볼링공을 고르려고 한다. N = 볼링공의 개수
#공의 무게는 1 ~ M까지 순서대로 부여되며 자연수 형태이다.(자연수 1~10)

n,m = map(int, input().split())
weight = list(map(int, input().split()))
x = 1 #반복문에서 range 제어하려고
cnt = 0 #무게 중복된 횟수

for i in range(len(weight)) :
 
    for j in range(x,len(weight)) :
      
        if weight[i] == weight[j] :
            cnt += 1
            
    x += 1

 
total = (n*(n-1)) / 2 #볼링공이 총 n개 일때 나올 수 있는 경우의 수
result = int(total) -cnt #경우의 수에서 중복 제거 
print(result)
    