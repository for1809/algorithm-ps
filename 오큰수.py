'''
문제
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.


'''
'''
# 정말 원시적인 방법
n = int(input())
seq = list(map(int, input().split()))
result = []
for i, v in enumerate(seq):
    flag = 1
    for j in seq[i + 1:]:
        if j > v:
            result.append(j)
            flag = 0
            break
    if flag:
        result.append(-1)
print(result)
'''
# 시간복잡도 O(n2) 당연히~ 시간초과

# 스택 활용
n = int(input())
seq = list(map(int, input().split()))
result = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    v = seq[i]
    if stack:
        while True:
            if stack[-1] > v:
                result[i] = stack[-1]
                stack.append(v)
                break
            elif stack[-1] <= v:
                stack.pop()
            if not stack:
                stack.append(v)
                break
    else:
        stack.append(v)
print(' '.join(map(str,result)))

