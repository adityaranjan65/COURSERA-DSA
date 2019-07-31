# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    current_refills = 0
    last_refills = 0
    
    stops.append(distance)
    stops.insert(0,0)
    n=len(stops)
    #print("Stops where you need to get refilling:")
    while current_refills < (n-1):
        last_refills = current_refills
        while ((stops[current_refills + 1] - stops[last_refills]) <= tank):
                current_refills = current_refills + 1
                if current_refills == (n - 1):
                    break
        if current_refills == last_refills:
            
            return -1
        if current_refills < (n - 1):
            num_refills = num_refills + 1
    
    return num_refills

if __name__ == '__main__':
    d=int(input())
    m=int(input())
    n=int(input())
    stops = list(map(int, input().strip().split()))
    print(compute_min_refills(d, m, stops))
