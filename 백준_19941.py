N, K = map(int, input().split()) #두 숫자(길이N, 거리 K)를 입력받아 정수로 저장
table = list(input().strip()) #문자열을 문자 하나하나 리스트로 바꿈, strip()은 끝에 붙는 엔터를 제거하는 역할

count = 0
for i in range(N): 
    if table[i] == 'P':  # 사람일 때
        # i-K ~ i+K 범위에서 햄버거 찾기
        start = max(0, i - K) # 사람이 닿을 수 있는 왼쪽 끝위치 계산, 최솟값을 0 (음수로 나가면 안됨) 
        end = min(N - 1, i + K) #사람이 닿을수 있는 오른쪽 끝 위치 계산, 범위 벗어나지 않게 최대값 N-1 
        for j in range(start, end + 1): #닿을수 있는 범위 차례로 훑기
            if table[j] == 'H': #햄버거 o (아직 안 먹힌 햄버거이면)
                table[j] = 'X'  # 먹힌 햄버거 표시
                count += 1 
                break

print(count)
