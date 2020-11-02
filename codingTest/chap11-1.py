#모험가 N명이 있다. 
#공포도가 x인 사람은 반드시 x명 이상으로 팀을 구성해야한다.
#최대 모험가 그룹을 구하여라
n = int(input())
data = list(map(int, input().split()))
group_people = 0
group_cnt =0
#공포도 높,낮 -> [2,3,1,2,2,] 이렇게 되어있는 것을 정렬
data.sort() 
print(data)
#우선 그룹에 사람들을 한명씩 넣고 그룹에 들어간 사람의 수와 들어온 사람의 분포도가 맞으면 
#그룹의 수가 1개 증가
 
for i in data :
  group_people += 1 #for가 한번 돌면 그룹에 사람에 한명 들어온 것 

  if i <= group_people : #그룹에 누적된 인원 수가 방금 들어온 공포도가 같거나 크면
      group_cnt += 1 #그룹수 +1
      group_people -= i #그룹에 들어와있던 사람들이 그룹지어 나갔으니 빼줘야함

print(group_cnt)

