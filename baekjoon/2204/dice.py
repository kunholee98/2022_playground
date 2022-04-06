N = int(input())
nums = list(map(int, input().split()))

# 중앙면적: (N-2)*(N-1)*4 + (N-2)*(N-2)
# 모서리: (N-2)*4 + (N-1)*4
# 꼭짓점: 4

a = min(nums[0], nums[5])
b = min(nums[1], nums[4])
c = min(nums[2], nums[3])

abc = sorted([a,b,c])

if N == 1:
    print(sum(sorted(nums)[:5]))
else:
    print(abc[0]*((N-2)*(N-1)*4+(N-2)*(N-2)) + sum(abc[0:2])*((N-2)*4+(N-1)*4) + sum(abc)*4)