n,m = map(int, input().split())

result = 0

for i in range(n) : #n개 행을 받을거니까 첫번째 행일때 ~ n번째 행일때까지 반복해서 data 받음 
    data = list(map(int, input().split()))#list =[1,2,3]이형태로 받음
    min_value = min(data) #입력받은 data에서 가장 작은 값을 구하고 min_value에 저장하고 
    #print(min_value)
    result = max(result, min_value) #data에서 도출한 min_value를 result에 넣고 max(안에서 result,min_value 비교)
    #print(result)
print(result)
  

#max는 리스트 외에 요소끼리만 비교 가능
'''  
a,b = map(int, input().split())
maxresult =  max(a,b)
print(maxresult)
'''