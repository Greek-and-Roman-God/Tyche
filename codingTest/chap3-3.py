n,m = map(int, input().split())

result = 0

for i in range(n) : #n개 행을 받을거니까 첫번째 행일때 ~ n번째 행일때까지 반복해서 data 받음 
    data = list(map(int, input().split()))#list =[1,2,3]이형태로 받음
    min_value = min(data) #입력받은 data에서 가장 작은 값을 구하고 min_value에 저장하고 
    #print(min_value)
    result = max(result, min_value) #data에서 도출한 min_value를 int형 리스트인 result에 넣고 max가 result에 저장된 요소 중 가장 큰 값을 도출함 
    #print(result)
print(result)
  
  
