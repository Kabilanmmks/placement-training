
n = int(input())
english_subscribers = set(map(int, input().split()))
m = int(input())
french_subscribers = set(map(int, input().split()))
both_subscribers = english_subscribers.intersection(french_subscribers)

print(len(both_subscribers))
