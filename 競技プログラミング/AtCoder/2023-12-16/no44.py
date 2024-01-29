N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    u,v = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    
if len(G[0]) == 1:
    print(1)
    exit()
ans = 0
l = []
print(G)

def dfs(pos):
    seen = [0]*N
    seen[pos] = 1
    for node in G[pos]:
        
        cnt = 1
        stack = [node]
        
        while stack:
            print(stack)
            print(seen)
            n = stack.pop()
            seen[n] = 1
            for g in G[n]:
                if seen[g] == 0:
                    stack.append(g)
                    cnt += 1
        l.append(cnt)

dfs(0)
l = sorted(l)
print(sum(l)-l[-1]+1)
        