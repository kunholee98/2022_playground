N = int(input())
P = 1000000007
cnt = 0
def power(n):
    if n == 1:
        return [1,1,1,0]
    half = power(n//2)
    return multi(multi(half,half),[1,1,1,0]) if n%2 else multi(half, half)

def multi(A,B):
    a = ((A[0]*B[0])%P + (A[1]*B[2])%P)%P
    b = ((A[0]*B[1])%P + (A[1]*B[3])%P)%P
    c = ((A[2]*B[0])%P + (A[3]*B[2])%P)%P
    d = ((A[2]*B[1])%P + (A[3]*B[3])%P)%P
    return [a,b,c,d]
if N == 1:
    print(1)
else:
    print(power(N-1)[0]%1000000007)