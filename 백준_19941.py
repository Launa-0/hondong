N, K = map(int, input().split())
table = list(input().strip())

count = 0
for i in range(N):
    if table[i] == 'P':  # 사람일 때
        # i-K ~ i+K 범위에서 햄버거 찾기
        start = max(0, i - K)
        end = min(N - 1, i + K)
        for j in range(start, end + 1):
            if table[j] == 'H':
                table[j] = 'X'  # 먹힌 햄버거 표시
                count += 1
                break

print(count)
