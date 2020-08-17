
class Heap:
    def __init__(self, nums):
        self.nums = nums
        print (self.nums)

    def heapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        if left < len(self.nums) and self.nums[left] > self.nums[i]:
            largest = left
        else:
            largest = i

        if right < len(self.nums) and self.nums[right] > self.nums[largest]:
            largest = right

        if largest != i:
            temp = self.nums[largest]
            self.nums[largest] = nums[i]
            self.nums[i] = temp
            self.heapify(largest)


    def heap_tree(self) -> list:
        for i in range(int(len(self.nums) / 2), -1, -1):
            self.nums = self.heapify(i)
        return self.nums

    def heap_sort(self):
        pass

if __name__ == "__main__":
    nums = [1, 4, 20, 3, 10, 5, 33, 0]
    hp = Heap(nums)
    nums = hp.heap_tree()
    print (nums)
    # ans [[2, 4], [6, 6], [6, 7]]
