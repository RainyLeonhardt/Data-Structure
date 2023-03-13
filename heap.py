import heapq
nums = [5, 40, 3, 1, 2, 70, 8]

heapq.heapify(nums)
print(nums)

print(heapq.heappop(nums))
print(heapq.heappop(nums))
print(heapq.heappop(nums))

nums = [5, 40, 3, 1, 2, 70, 8]
heapq.heapify(nums)
res = []
i = 0
N = len(nums)
while i < N:
    res.append(heapq.heappop(nums))
    i += 1

print(res[::-1])