#지금까지 나온 주유소 중 가장 싼 가격으로 계속 기름을 넣는다
#싼 주유소를 만나면 그 뒤에 오는 도로까지 한꺼번에 채워가는 것이 유리
# 주유소 문제 (백준 13305)

N = int(input().strip())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

total_cost = 0
min_price = prices[0]

for i in range(N - 1):  # 마지막 도시는 도로 없음
    # 지금까지 가장 싼 주유소 가격으로 이동
    total_cost += min_price * distances[i]
    # 다음 도시의 주유소 가격이 더 싸면 갱신
    if prices[i + 1] < min_price:
        min_price = prices[i + 1]

print(total_cost)
