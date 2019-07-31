# Uses python3
import sys

def gcd_naive(a, b):
    if(b==0):
        return(a)
    else:
        c=a%b
        return(gcd_naive(b,c))

    return(0)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
