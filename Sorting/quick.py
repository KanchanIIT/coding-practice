class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def partition(self, l, h):
        i, pivot = l - 1, h
        for j in range(l, h):
            if self.nums[j] < self.nums[pivot]:
                i += 1
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        self.nums[i + 1], self.nums[h] = self.nums[h], self.nums[i + 1]
        return i+1

    def sort(self, l, h):
        if l < h:
            pivot = self.partition(l, h)
            self.sort(l, pivot - 1)
            self.sort(pivot + 1, h)


nums = [11, 7, 8, 2, 23, 43, 12, 5, 4]
qs = QuickSort(nums)
qs.sort(0, len(nums) - 1)
print(qs.nums)
