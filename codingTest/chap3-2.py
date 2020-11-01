#큰 수 법칙 여러수로 이루어진 배열이 있을때  M번 더해 연속해서 k번 초과하지 않고 가장 큰 수 구하기
#가장 큰 수 1개, 연속적으로 사용할때 제약있으니 중간에 넣어줄 두번째로 큰 수 1개가 필요함.
#n은 배열크기, m은 몇번 더하는지, k는 연속해서 k까지 사용가능

n, m, k = map(int, input().split()) # n=1,m=2,k=3 이런 형태로 저장됨

list = list(map(int, input().split()))
list.sort() #배열에 질서없이 들어가있는 숫자를 정렬 하면 제일 큰 수 구하기 쉬움
result = 0 
#print(list)
first = list[n-1] #배열의 크기는 n이니 가장 큰 수는 n-1
second = list[n-2] 

#print(first)
#print(second)

while 1 : #무한루프
  for i in range(k) : #최대 k번 연속으로 쓸 수 있으니 k번 for문 돌리면서 first 더해주면 됨
    if m==0 : #m(더하는 수)가 m이면 반복을 돌릴 수 없다.
      break
    result += first
    m -= 1  #더했으면 m에서 빼줘야함
  if m==0 :
    break #first를 k만큼 연속으로 더하고 second를 더해줘야하지만 m이 0이면 더할 수 없으니 break
  result += second
  m -= 1  #second 더해줬으니 m에서 빼주기

print(result)

  





