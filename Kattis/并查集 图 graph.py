# 定义并查集的 find 和 union 操作
def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i]) # 路径压缩
    return parent[i]

def union(parent, i, j):
    parent[find(parent, i)] = find(parent, j)

# 读入输入
N, K, M = map(int, input().split())

# 初始化 parent 数组
parent = list(range(N+1))

# 合并连通块
for _ in range(M):
    a, b = map(int, input().split())
    if a != K and b != K:
        union(parent, a, b)

# 检查是否能够战胜敌对领袖
for i in range(1, N+1):
    if i == K:
        continue
    if find(parent, i) != find(parent, K):
        print(i,K)
        break
else:
    print("NO")