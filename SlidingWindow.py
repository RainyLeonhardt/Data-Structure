from random import randint


class solution:
    def __init__(self, l) -> None:
        self.l = l
    def slidingwindow(l, k):
        res = []
        num = sum(l[:k])
        res.append(num)
        left = 0
        for i in range(k, len(l)):
            num -= l[left]
            num += l[i]
            res.append(num)
            left += 1
            print(res)
        return res
    def bruteforce(l, k):
        res = []
        for i in range(len(l) - k + 1):
            res.append(sum(l[i:i + k]))
        return res

nums = []
for _ in range(10**3):
	value = randint(0, 100)
	nums.append(value)

# nums = [1,5,74,2,6,7,4,5,98,4,8,8,9,54,7,7,1]

# print(solution.slidingwindow(nums, 3))
print(solution.bruteforce(nums, 3))

