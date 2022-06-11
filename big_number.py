# 큰수의 법칙 | 주어진 수를 M번 더하여 가장 큰 수를 만드는 법칙.

# 배열의 크기 N 숫자가 더해지는 횟수 M 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

# N, M, K를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

#데이터 정렬
data.sort()
first = data[n-1] #가장 큰수
second = data[n-2] #두번째로 큰수

result = 0

while True:
	for i in range(k): # 가장 큰 수를 K번 반복
		if m == 0:
			break
		result += first
		m -= 1
	if m == 0:
		break
	result += second
	m -= 1
	
print(result)
