from queue import PriorityQueue

def solution(food_times, k):
  if sum(food_times) <= k : #먹을 음식의 개수가 k가 크거나 같으면 다 먹은거니까 -1을 return
      return -1
  answer = 0

  q = PriorityQueue() #큐를 만들고
  for i in range(len(food_times)) : #모든 음식들을
     q.put((food_times[i], i+1)) #우선 순위 큐에 넣는다.(튜플의 첫번째 원소 : 음식의 시간 -> 원소가 음식의 시간으로 오름차순으로 될 수 있음))
  sum_value = 0
  previous = 0
  length = len(food_times)

  while sum_value + ( (q.queue[0][0] - previous) * length ) <= k: #1.시간이 적게 걸리는 음식부터 하나씩 확인하고 2. 빼야될 값이 k보다 커졌을때 while문 탈출
      now = q.get()[0] #음식
      sum_value +=(now - previous) * length #그 이전에 먹었던 음식과의 그 시간차 만큼 현재 남아있는 음식들의 개수와 곱하면 됨
      length -= 1
      previous = now

  #남은 음식중에서 몇 번째 음식인지 확인
  target = k - sum_value + 1 #타켓을 남ㅇ
  length = len(q.queue)
  temp = (target - 1) // length
  result = sorted(q.queue, key=lambda x : x[1]) #음식의 번호를 기준으로 정렬
  target -= temp * length
  return result[target -1][1] #타켓의 번호를 출력하면 됨
    
