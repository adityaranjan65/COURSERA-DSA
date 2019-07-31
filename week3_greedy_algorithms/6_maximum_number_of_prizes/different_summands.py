# Uses python3
import sys

def get_max_pairwise_sum(n):
    pairs = list()
    pairs.append(1)
    temp = 2
    while n != 0:
        if n > (temp * 2):
            pairs.append(temp)
            n -= temp
            temp += 1
        else:
            pairs.append(n)
            break
    print(len(pairs))
    for x in pairs:
        print(x, end=' ')

def main():
    num = int(input())
    
    if num <= 2:
        print("1\n", num)
    else:
        get_max_pairwise_sum(num - 1)
    
if __name__ == "__main__":
    main()
    
