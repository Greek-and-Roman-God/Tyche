#0과 1로만 구성된 문자열을 입력받는다.
#이어진 문자열을 한번에 뒤집을 수 있다. 
#이 경우 모두 같은 수로 만드려면 최소 몇번 시행되어야 하나
#모두 0으로 만들었을때 몇번 뒤집었는지 1 -> 0 : cnt0,
#모두 1으로 만들었을때 몇번 뒤집었는지 0 -> 1 : cnt1 
data = input()

cnt0 = 0
cnt1 = 1 

for i in range(len(data)-1) : #data[i]와 data[i+1] 비교해야하니 data길이 보다 -1 적게 돌아야 함 
    if data[i] == data[i+1] : pass # 0 0 or 1 1 인 경우는 pass

    else : #data[i] != data[i+1] 다른 경우 뒤집어야 함 
        if data[i+1] == '1' : #data는 문자열임 이 경우는 0 1일 때
          cnt0 += 1
        else :
          cnt1 += 1 
print(min(cnt0,cnt1))


#'연속'때문에 헷갈렸던 이유 : 값을 세면서 동시에 갑을 변경하는 것으로 생각함 
#00110이면 
# data[0] = 0 / data[1] = 0 값 같으니 -> pass 
# data[1] = 0 / data[2] = 1 값 다르고 data[i+1]이 1이니 -> cnt0 +=1 
# data[2] = 1 / data[3] = 1 값 같으니 -> pass  이 부분에서 data[2]가 0으로 변경됐다고 생각해서 꼬임.. 