# 입력 및 출력
c = input()
print(c)

c = input()
c = int(c)
print(c)

a,b = input().split()
print(b,a)

# 출력 print 시 옵션, sep, end
a,b = input().split(':')
print(a,b,sep=':',end=' ')

#10진수를 16진수로 전환
a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력
print('%X' % n)  #n에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력

#16진수를 입력받아 8진수로 전환
a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

# 

#영문자를 받아 10진수 유니코드 값으로 출력
n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
print(n)

#문자를 받아 다음 문자 출력하기 - 유니코드 이용
n = ord(input())
print(chr(n+1))  #유니코드 받아 1을 더하고 문자로 전화하면 다음 문자이다

# 정수를 받아 부호 변경하며 출력
n = input()
print(-n) 

#단어와 반복 횟수를 1번 입력받아 여러 번 출력해보자.
w, n = input().split()
print(w*int(n))

#단어와 반복 횟수를 2번 입력받아 여러 번 출력해보자.
n = input()
s = input()
print(int(n)*s)

#실수 1개를 입력받아 소숫점 이하 두 번째 자리로 반올림 후 출력
a=float(input())
print( format(a, ".2f") )

# 비트연산자
# 정수 10의 2진수 표현은 ... 1010 이다.
# 10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
# 10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.
n = 10
print(n<<1)  #10을 2^1배 한 값인 20 이 출력된다.
print(n>>1)  #10을 2^-1한 값인 5 가 출력된다.
print(n<<2)  #10을 2^2배 한 값인 40 이 출력된다.
print(n>>2)  #10을 2^-2 한 값인 2 가 출력된다.

# 논리연산 - XOR
# 참 거짓이 서로 다를 때에만 True 로 계산하는 논리연산을 XOR(exclusive or, 배타적 논리합) 연산이라고도 부른다.
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 3항 연산
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값
0 if 123>456 else 1

# 3항연산으로 가장 큰 수 확인
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 3항연산으로 가장 큰 수 확인
a, b, ㅊ = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = int(c)
d = (a if a>b else b) if ((a if a>b else b)>c) else c
print(int(d))

# 평가를 문자로 입력받아 코멘트를 출력하자
a =  input()
dict = {'A':'Good', 'D': 'Bad'}
print(dict[a] if a in dict else 'what?')


# 정수 1개 입력받아 카운트다운 출력하기
n = input()
while n!=0 :
  print(n)
  n = n-1

# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1


