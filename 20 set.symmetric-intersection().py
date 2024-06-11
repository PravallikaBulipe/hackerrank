def students_with_either_subscription_but_not_both(english, french):
    english_set = set(english)
    french_set = set(french)
    either_subscription_but_not_both = english_set.symmetric_difference(french_set)
    return len(either_subscription_but_not_both)
n = int(input())
english = list(map(int, input().split()))
b = int(input())
french = list(map(int, input().split()))
print(students_with_either_subscription_but_not_both(english, french))
