# Uses python3
import sys

def get_change(m):
    a=[10,5,1]
    count=0
    while(m>0):
        for i in a:
            if(m/i>0):
                count+=m//i
                m=m%i
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
