#숫자(0~9)로만 이루어진 문자열 s를 주어졌을때 왼쪽부터 오른쪽까지 숫자를 확인하여 숫자 사이에 + or * 를 넣어
#가장 큰 수를 만들어라. 단, 원래 연산과는 다르게 왼쪽부터 오른쪽까지 순서대로 진행된다. 
# 1.문자열이니 int로 변경해줘야 연산할 수 있음
# 2. x  y 사이에 연산자를 넣을때 x, y 모두 0,1 어느 것도 해당되지 않아야 * 연산자가 가능 1 * 3 < 1+3 이고 0 * 3은 안되니까
# 3. data[0]은 total에 for문안에서 안넣고 미리 넣은게 x  y 이렇게 비교해야하는데 data[0]를 for문 안에서 넣으면 
#비교대상이 없어서 굳이 for문 안에서 data[0]부터 쭉 넣고 싶으면 경우의 수 찾아서 걸러줘야함

data = input() #문자열로 받음
total = int(data[0]) #문자열로 받았으니 int로 변환해야 연산가능
ele = 0

for i in range(1,len(data)) : #data[0]요소는 넣었으니 data[1]부터 돌려야 하고 len(data)는 data의 길이 즉, n임 
                              #range(1,n)은 1부터 n-1까지니 data[1] ~ data[n-1]까지 넣을 수 있다!!.
    ele = int(data[i])
    if ele <=1 or total <= 1 :
        total += ele
    else :
        total *= ele
print(total)