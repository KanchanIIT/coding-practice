class HeapSort:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(self.nums)

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        if left < self.size and self.nums[left] > self.nums[i]:
            largest = left
        else:
            largest = i
        if right < self.size and self.nums[right] > self.nums[largest]:
            largest = right

        if largest != i:
            self.nums[largest], self.nums[i] = self.nums[i], self.nums[largest]
            self.heapify(largest)

    def create_heap_tree(self):
        for i in range(int(len(self.nums) / 2), -1, -1):
            self.heapify(i)

    def sort(self):
        while self.size > 0:
            self.nums[0], self.nums[self.size - 1] = self.nums[self.size - 1], self.nums[0]
            self.size = self.size - 1
            self.heapify(0)


nums = [11, 7, 8, 2, 23, 43, 12, 5, 4]
hs = HeapSort(nums)
hs.create_heap_tree()
hs.sort()
print(hs.nums)
