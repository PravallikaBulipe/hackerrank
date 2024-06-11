def average(array):
    distinct_heights=set(arr)
    total_sum=sum(distinct_heights)
    count_distinct=len(distinct_heights)
    avg=total_sum/count_distinct
    return round(avg,3)
    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
