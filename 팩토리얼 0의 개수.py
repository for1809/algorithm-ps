'''
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
'''
import numpy as np
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def margin(n, m):
    if np.log(n) < m:
        return 0
    return m - 1 if n % 10 ** m != 0 else margin(n, m + 1)

n = factorial(int(input()))
print(margin(n, 1))