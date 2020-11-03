#동전 N개로 만들 수 없는 최소값을 구하시오
n = int(input())
data = list(map(int, input().split()))
data.sort()

impossible_p = 1 #만들수 없는 최소값이니 1부터 시작 0부터는 의미 X

for i in data :
    if impossible_p < i :
        break
    impossible_p += i
print(impossible_p)

# impossible_p |   i
#       1      |   1
#       2      |   1
#       3      |   2
#       5      |   3
#       8      |   9  -> impossible_p 보다 i가 크면 impossible_p를 만들지 못함



