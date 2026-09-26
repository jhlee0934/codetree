N = int(input())

# Please write your code here.

def facto(N):
    if N == 0:
        return 1
    
    return N*facto(N-1)

print(facto(N))