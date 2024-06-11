def check_subset(test_cases):
    results = []
    for _ in range(test_cases):
        num_elements_a = int(input())
        set_a = set(map(int, input().split()))
        num_elements_b = int(input())
        set_b = set(map(int, input().split()))
        if set_a.issubset(set_b):
            results.append("True")
        else:
            results.append("False")
    for result in results:
        print(result)
T = int(input())
check_subset(T)
