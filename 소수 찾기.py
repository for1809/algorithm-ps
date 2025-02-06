'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
'''
n = int(input())
n_lst = list(map(int, input().split()))
result = [1] * n
for j in range(n):
    num = n_lst[j]
    if num == 2:
        continue
    if num == 1 or num % 2 == 0:
        result[j] = 0
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            result[j] = 0
            break

print(sum(result))