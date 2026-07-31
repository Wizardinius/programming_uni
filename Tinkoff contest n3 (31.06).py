a,b = map(int, input().split())

def gcd(a,b):
    return (a if b==0 else gcd(b,a%b))

def lcm(a,b):
    return a*b/gcd(a,b)

print(int(lcm(a,b)))