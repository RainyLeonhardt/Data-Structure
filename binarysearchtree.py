# def binarySearch(nums, low, high, x):
#     if high < low:
#         return None
#     mid = (low + high)//2
#     if nums[mid] == x:
#         return mid
#     elif nums[mid] > x:
#         return binarySearch(nums, low, mid-1, x)
#     else:
#         return binarySearch(nums, mid+1, high, x)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(binarySearch(nums, 0, len(nums) - 1, 4))
# print(binarySearch(nums, 0, len(nums) - 1, 9))
# print(binarySearch(nums, 0, len(nums) - 1, 40))

class bs(object):

    def binarySearch(arr, target):
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target > arr[mid]:
                L = mid + 1
            elif target < arr[mid]:
                R = mid - 1
            else:
                return mid
        return -1

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bs.binarySearch(nums, 9))
