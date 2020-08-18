import math


class Heap:
    def __init__(self):
        self.stones = list()
        self.value = None
        self.size = 0

    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        if left < self.size and self.stones[left] > self.stones[i]:
            largest = left
        else:
            largest = i
        if right < self.size and self.stones[right] > self.stones[largest]:
            largest = right

        if largest != i:
            temp = self.stones[largest]
            self.stones[largest] = self.stones[i]
            self.stones[i] = temp
            self.heapify(largest)


    def lastStoneWeight(self, stones):
        self.stones = stones
        self.size = len(self.stones)
        for i in range(math.floor(len(self.stones) / 2), -1, -1):
            self.heapify(i)

    def heap_sort(self):
        while self.size > 1:
            temp = self.stones[0]
            self.stones[0] = self.stones[self.size - 1]
            self.stones[self.size - 1] = temp
            self.size = self.size - 1
            self.heapify(0)



if __name__ == "__main__":
    nums = [1, 4, 20, 3, 10, 5, 33, 0]
    hp = Heap()
    hp.lastStoneWeight(nums)
    hp.heap_sort()
    print (hp.stones)
    # ans [[2, 4], [6, 6], [6, 7]]
