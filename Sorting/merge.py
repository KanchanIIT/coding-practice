class Merge:
    def __init__(self, nums):
        self.nums = nums

    def merge(self, first, second):
        m = n = 0
        res = list()
        while(m< len(first) and n<len(second)):
            if first[m]<second[n]:
                res.append(first[m])
                m+=1
            else:
                res.append((second[n]))
                n+=1
        while(m<len(first)):
            res.append(first[m])
            m+=1
        while(n<len(second)):
            res.append((second[n]))
            n+=1
        return res

    def sort(self, l, h):
        if l>=h:
            return
        mid = int((l+h)/2)
        self.sort(l,mid)
        self.sort(mid+1, h)
        combined = self.merge(self.nums[l:mid+1], self.nums[mid+1:h+1])
        self.nums[l:h+1] = combined





nums = [11, 7, 8, 2, 23, 43, 3,1,32,2,6,9,5,4,4,4,4]

ms = Merge(nums)
ms.sort(0, len(nums)-1)
print (ms.nums)


