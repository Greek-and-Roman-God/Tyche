'''
a,b = map(int, input().split())

if a > b :
    print(">")
elif a < b :
    print("<")
elif a == b :
    print("==")
'''
# 백준 왜 위에 코드는 틀렸다고 하지..
'''
grade = int(input())

if 90 <= grade :
    print("A") 
elif 80 <= grade and grade < 90 :
    print("B")
elif 70 <= grade and grade < 80 :
    print("c")
elif 60 <= grade and grade < 70 :
    print("D")
elif 60 > grade :
    print("F")


grade = int(input())

if grade >= 90 :
    print("A")
elif grade >= 80 and grade < 90 :
    print("B")
elif grade >= 70 and grade < 80 :
    print("C")
elif grade >= 60 and grade < 70 :
    print("D")
elif grade < 60 :
    print("F")

'''
#윤년 조건1 연도가 4의 배수이면서 100의 배수가 아닐때 
#조건2 연도가
'''
year = int(input())

if year % 4 == 0 and ( (year % 100 != 0) or (year % 4 == 0) ):
    print(1)
else : 
    print(0)
'''

#1,2,3,4분면 구하기
'''
x = int(input())
y = int(input())
 
if x > 0 and 0 < y :
    print(1)
if x < 0 and 0 < y :
    print(2)
if x < 0 and 0 > y :
    print(3)
if x > 0 and 0 > y :
    print(4)
'''

h,m = map(int, input().split())

if m-45 < 0 :
    if h == 0 :
        h = 24
    h -= 1
    m = m-45+60
    print(h, m)
elif m-45 == 0 :
    m -=45
    print(h, m)
elif m-45 > 0 :
    m -=45
    print(h, m)







